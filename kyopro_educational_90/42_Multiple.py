K = int(input())
if K % 9 != 0:
    print(0)
    exit()
mod = 10**9+7
dp = [0]*(K+10)
dp[0] = 1
for i in range(1, K+1):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4]+dp[i-5]+dp[i-6]+dp[i-7]+dp[i-8]+dp[i-9]
    dp[i] %= mod
print(dp[K])
