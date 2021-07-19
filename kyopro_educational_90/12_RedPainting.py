from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

H, W = map(int, input().split())
uf = UnionFind(H*W)
Q = int(input())
field = [[0]*W for h in range(H)]
dh = [1,-1,0,0]
dw = [0,0,1,-1]

def convert(h, w):
    return W*h+w

for q in range(Q):
    l = list(map(int, input().split()))
    if l[0] == 1:
        h, w = l[1]-1, l[2]-1
        field[h][w] = 1
        x = convert(h, w)
        for i in range(4):
            nh = h+dh[i]
            nw = w+dw[i]
            if 0 <= nh < H and 0 <= nw < W and field[nh][nw]:
                nx = convert(nh, nw)
                uf.union(x, nx)
    else:
        h1, w1, h2, w2 = l[1]-1, l[2]-1, l[3]-1, l[4]-1
        x1 = convert(h1, w1)
        x2 = convert(h2, w2)

        if uf.same(x1, x2) and field[h1][w1] and field[h2][w2]:
            print('Yes')
        else:
            print('No')
