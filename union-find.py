import random

class Union_find:
    def __init__(self, n=1):
        self.n = n
        self.adj = {i: [] for i in range(self.n)}
        self.parent = [i for i in range(self.n + 1)]
        self.rank = [1] * (self.n + 1)
        self.build_adj()
        print(self.adj)

    def build_adj(self):
        for i in range(1, self.n):
            self.adj[i].append(random.randint(1, self.n))
            self.adj[i].append(random.randint(1, self.n))

        
    def find(self, node):
        p = self.parent[node]
        while p != self.parent[node]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[node]
        return p


    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p1
            self.rank[p2] += self.rank[p1]

        return True
        
    def cycle(self):
        for _, val in self.adj.items():
            if val:
                x, y = val
                if not self.union(x, y):
                    print('edges are already connected', [x, y])
                    print('rank', self.rank)
                    return [x, y]
        print('rank', self.rank)


u = Union_find(5)

u.cycle()


