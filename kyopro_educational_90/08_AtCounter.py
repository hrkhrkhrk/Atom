N = int(input())
S = input()
A = 'atcoder'
M = len(A)
mod = 10**9+7
dp = [[0]*(N+1) for i in range(M+1)]

for j in range(N+1):
    dp[0][j] = 1

for i in range(1, M+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1]
        if S[j-1] == A[i-1]:
            dp[i][j] += dp[i-1][j-1]
            dp[i][j] %= mod
print(dp[-1][-1])
