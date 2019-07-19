from collections import defaultdict
class Queue:
    def __init__(self):
        self.queue = []
    def add(self, x):
        self.queue.append(x)
    def pop(self):
        return self.queue.pop(0)
    def len(self):
        return len(self.queue)

class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n
    def connect(self, x, y):
        self.graph[x+1].append(y+1)
        self.graph[y+1].append(x+1)
    def find_all_distances(self, s):
        start = s + 1
        graph = self.graph

        queue = Queue()
        queue.add(start)
        dist = {}
        parents = {}

        output_arr = []

        for node in graph:
            dist[node] = -1

        dist[start] = 0

        while queue.len() > 0:
            node = queue.pop()
            for nbr in graph[node]:
                if nbr not in parents:
                    parents[nbr] = node
                    dist[nbr] = dist[node] + 6
                    queue.add(nbr)

        for i in range(1, self.n + 1):
            if i == start:
                continue
            if i not in dist:
                output_arr.append("-1")
            else:
                output_arr.append(str(dist[i]))

        print ' '.join(output_arr)




t = input()
for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x-1,y-1)

    s = input()
    graph.find_all_distances(s-1)
