# Author: Nguyen_DD
import sys

sys.setrecursionlimit(200000)

class DSU:
    def __init__(self, n):
        self.par = [-1] * (n + 1)
        self.fall = [-1] * (n + 1)

    def find_set(self, u):
        if self.par[u] < 0:
            return u
        return self.find_set(self.par[u])

    def merge_set(self, u, v):
        u = self.find_set(u)
        v = self.find_set(v)
        if u != v:
            if self.par[u] > self.par[v]:
                u, v = v, u
            if v == 1:
                u, v = v, u
            self.par[u] += self.par[v]
            self.par[v] = u

    def get(self, u):
        while u > 0:
            if self.fall[u] != -1:
                return self.fall[u]
            u = self.par[u]
        return -1

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)

    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        adj = [[None, [0, False], [0, False]] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            adj[i][1][0] = int(next(iterator))
            adj[i][2][0] = int(next(iterator))
            
        queries = []
        for _ in range(m):
            u = int(next(iterator))
            side = int(next(iterator))
            queries.append((u, side))
            adj[u][side][1] = True
            
        dsu = DSU(n)
        
        for i in range(1, n + 1):
            for j in range(1, 3):
                target, removed = adj[i][j]
                if not removed and target > 0:
                    dsu.merge_set(i, target)
                    
        for i in range(m - 1, -1, -1):
            u_idx, side = queries[i]
            v_idx = adj[u_idx][side][0]
            
            u = dsu.find_set(u_idx)
            v = dsu.find_set(v_idx)
            root_one = dsu.find_set(1)
            
            if v == root_one:
                u, v = v, u
            
            if u == root_one:
                if v == root_one:
                    continue
                dsu.fall[v] = i
                dsu.merge_set(u, v)
            else:
                dsu.merge_set(u, v)
                
        output = []
        for i in range(1, n + 1):
            output.append(str(dsu.get(i)))
        sys.stdout.write('\n'.join(output) + '\n')
            
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()