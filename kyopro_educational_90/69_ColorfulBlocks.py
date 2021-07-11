N, K = map(int, input().split())
mod = 10**9+7
if N == 1:
    ans = K
elif N == 2:
    if K > 1:
        ans = K*(K-1)%mod
    else:
        ans = 0
else:
    if K > 2:
        ans = K*(K-1)
        n_2 = [int(n) for n in bin(N-2)[::-1][:-2]]
        m = [0]*len(n_2)
        m[0] = K-2
        ans *= m[0]**n_2[0]
        for i in range(1, len(n_2)):
            m[i] = m[i-1]**2%mod
            if n_2[i]:
                ans *= m[i]
                ans %= mod
    else:
        ans = 0
print(ans)
