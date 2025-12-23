# Author: Nguyen_DD
import sys

sys.setrecursionlimit(200000)

class DSU:
    def __init__(self, n):
        self.par = [-1] * (n + 1)

    def find_set(self, u):
        if self.par[u] < 0:
            return u
        self.par[u] = self.find_set(self.par[u])
        return self.par[u]

    def merge_set(self, u, v):
        u = self.find_set(u)
        v = self.find_set(v)
        if u != v:
            if self.par[u] > self.par[v]:
                u, v = v, u
            self.par[u] += self.par[v]
            self.par[v] = u

    def get(self, u, v):
        u = self.find_set(u)
        v = self.find_set(v)
        return u == v

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
            k = int(next(iterator))
            
            for _ in range(m):
                next(iterator)
                next(iterator)
            
            queries = []
            for _ in range(k):
                s = next(iterator)
                u = int(next(iterator))
                v = int(next(iterator))
                queries.append((s, u, v))
            
            dsu = DSU(n)
            res = []
            
            for s, u, v in reversed(queries):
                if s == "cut":
                    dsu.merge_set(u, v)
                else:
                    res.append(dsu.get(u, v))
            
            output = []
            for val in reversed(res):
                output.append("YES" if val else "NO")
            
            sys.stdout.write('\n'.join(output) + '\n')
            
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()