N = int(input())
M = 1002
field = [[0]*M for h in range(M)]
paper = [[0]*M for h in range(M)]
for i in range(N):
    h0, w0, h1, w1 = map(int, input().split())
    field[h0][w0] += 1
    field[h1][w1] += 1
    field[h1][w0] += -1
    field[h0][w1] += -1
for h in range(M):
    for w in range(M):
        paper[h][w] = paper[h][w-1] + field[h][w]
for w in range(M):
    for h in range(M):
        paper[h][w] = paper[h-1][w] + paper[h][w]

ans = [0]*(N+1)
for h in range(M):
    for w in range(M):
        ans[paper[h][w]] += 1
for k in range(N):
    print(ans[k+1])
