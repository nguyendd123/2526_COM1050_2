# Author: Nguyen_DD
import sys

sys.setrecursionlimit(10**6 + 100)

class DSU:
    def __init__(self, n):
        self.par = [-1] * (n + 1)
        self.mn = list(range(n + 1))
        self.mx = list(range(n + 1))

    def find_set(self, u):
        if self.par[u] < 0:
            return u
        # Path compression
        self.par[u] = self.find_set(self.par[u])
        return self.par[u]

    def merge_set(self, u, v):
        u = self.find_set(u)
        v = self.find_set(v)
        
        if u != v:
            if self.par[u] > self.par[v]:
                u, v = v, u
            
            self.par[u] += self.par[v]
            self.mn[u] = min(self.mn[u], self.mn[v])
            self.mx[u] = max(self.mx[u], self.mx[v])
            self.par[v] = u

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
                
                if s == "union":
                    b = int(next(iterator))
                    dsu.merge_set(a, b)
                else:
                    root = dsu.find_set(a)
                    sys.stdout.write(f"{dsu.mn[root]} {dsu.mx[root]} {-dsu.par[root]}\n")
                    
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()