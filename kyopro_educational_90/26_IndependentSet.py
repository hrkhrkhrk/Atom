N = int(input())
X = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    X[a-1].append(b-1)
    X[b-1].append(a-1)

color = [[],[]]
q = [[0, -1, 0]]
while q:
    v, pv, c = q.pop()
    color[c].append(v+1)
    for i in X[v]:
        if i == pv: continue
        q.append([i, v, c^1])

if len(color[0]) >= N//2:
    for i in range(N//2):
        print(color[0][i])
else:
    for i in range(N//2):
        print(color[1][i])
