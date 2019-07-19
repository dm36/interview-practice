class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        # J represents the types of stones that are jewels
        # s represents the stones you have
        # want to know how many of the stones you have are also jewels

        return sum(j in J for j in S )

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        # J represents the types of stones that are jewels
        # s represents the stones you have
        # want to know how many of the stones you have are also jewels

        return len([j for j in S if j in J])

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for char in S:
            if char in J:
                count += 1
        return count
