from itertools import permutations
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
M = int(input())
X = [[True]*N for i in range(N)]
for i in range(M):
    x = list(map(int, input().split()))
    X[x[0]-1][x[1]-1] = False
    X[x[1]-1][x[0]-1] = False

List = []
inf = float('inf')
ans = inf

for k in permutations(range(N)):
    flag = True
    for i in range(N-1):
        if X[k[i]][k[i+1]] == False:
            flag = False
            break
    if flag:
        s = 0
        for j in range(N):
            s += A[k[j]][j]
        ans = min(ans, s)

if ans == inf:
    ans = -1
print(ans)
