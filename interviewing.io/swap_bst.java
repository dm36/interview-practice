import java.io.*;
import java.util.*;

/*
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Input -
   1
  /
 3
  \
   2


Output -
   3
  /
 1
  \
   2



  3 [-inf, +inf]
 / \  left: [-inf, 3], right: [3, +inf]
1   4 left:[3, 4] 2 -> [2, 4] 3
   /
  2




 */

class Solution {

  private static class Node {
    Node left, right;
    int val;
    Node(int v) {
     val = v;
    }
  }

  Node root;


  Node[] range = {new Node(Integer.MIN_VALUE), new Node(Integer.MAX_VALUE)};
  public static void main(String[] args) {
    Node root = buildTree();
    Solution s = new Solution();
    printInOrder(root);
    System.out.println();
    s.recoverBST(root);
    printInOrder(root);
  }

  private static Node buildTree() {
    Node root = new Node(3);
    root.left = new Node(1);
    root.right = new Node(4);
    root.right.left = new Node(2);
    return root;
  }

  private static void printInOrder(Node root) {
    if (root == null) return;
    printInOrder(root.left);
    System.out.println(root.val);
    printInOrder(root.right);
  }

  public void recoverBST(Node root) {
    if (root == null) return;
    this.root = root;
    helper(null, root);
  }



  private boolean helper(Node p, Node c) {
    if (c == null) return false;
    if (p != null) {
      if (c == p.left && c.val > p.val) {
        swap(c, p); // impl
        return true;
      }

      if (c == p.right && c.val < p.val) {
        swap(c, p); // impl
        return true;
      }
    }

    if (c.val < range[0].val) {
      swap(c, range[0]);
      return true;
    }

    if (c.val > range[1].val) {
      swap(c, range[1]);
      return true;
    }

    Node[] old = {range[0], range[1]};
    range[1] = c;
    if (helper(c, c.left)) return true;
    range[1] = old[1];
    range[0] = c;
    boolean right = helper(c, c.right);
    range[0] = old[0];
    return right;
  }

  private void swap(Node n1, Node n2) {
    int tmp = n1.val;
    n1.val = n2.val;
    n2.val = tmp;
  }


}


/*
Your previous Plain Text content is preserved below:

Welcome to your interviewing.io interview.

Once you and your partner have joined, a voice call will start automatically.

Use the language dropdown near the top right to select the language you would like to use.

You can run code by hitting the 'Run' button near the top left.

Enjoy your interview!
 */
