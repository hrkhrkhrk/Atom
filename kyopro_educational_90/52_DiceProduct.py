N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
x = 1
for i in range(N):
    x *= sum(A[i])
print(x%(10**9+7))
