N, M = map(int, input().split())
X = [[] for i in range(N)]
for i in range(1, M+1):
    x = list(map(int, input().split()))
    X[x[0]-1].append(x[1]-1)
    X[x[1]-1].append(x[0]-1)
n = 0
for i in range(N):
    if len([j for j in X[i] if j < i]) == 1:
        n += 1
print(n)
