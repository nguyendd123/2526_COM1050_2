# Author: Nguyen_DD
import sys

sys.setrecursionlimit(200000)

class DSU:
    def __init__(self, n):
        self.par = [-1] * (n + 1)
        self.added = [0] * (n + 1)

    def find_set(self, u, check=False):
        if self.par[u] < 0:
            return u
        p = self.find_set(self.par[u], True)
        if check and self.par[self.par[u]] > 0:
            self.added[u] += self.added[self.par[u]]
        self.par[u] = p
        return p

    def merge_set(self, u, v):
        u = self.find_set(u, True)
        v = self.find_set(v, True)
        if u != v:
            if self.par[u] > self.par[v]:
                u, v = v, u
            self.par[u] += self.par[v]
            self.added[v] -= self.added[u]
            self.par[v] = u

    def add_weight(self, u, w):
        u = self.find_set(u, True)
        self.added[u] += w

    def get(self, u):
        p = self.par[u]
        res = self.added[u]
        while p > 0:
            res += self.added[p]
            p = self.par[p]
        return res

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    try:
        t = 1
        for _ in range(t):
            n = int(next(iterator))
            m = int(next(iterator))
            dsu = DSU(n)
            
            for _ in range(m):
                s = next(iterator)
                a = int(next(iterator))
                if s == "join":
                    b = int(next(iterator))
                    dsu.merge_set(a, b)
                elif s == "add":
                    b = int(next(iterator))
                    dsu.add_weight(a, b)
                else:
                    sys.stdout.write(str(dsu.get(a)) + '\n')
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()