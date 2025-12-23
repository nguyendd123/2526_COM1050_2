# Author: Nguyen_DD

import sys

sys.setrecursionlimit(10**6 + 100)

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

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    dsu = DSU(n)
    output = []

    for _ in range(m):
        try:
            s = next(iterator)
            a = int(next(iterator))
            b = int(next(iterator))
            
            if s == "union":
                dsu.merge_set(a, b)
            else:
                root_a = dsu.find_set(a)
                root_b = dsu.find_set(b)
                output.append("YES" if root_a == root_b else "NO")
        except StopIteration:
            break
            
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == "__main__":
    solve()