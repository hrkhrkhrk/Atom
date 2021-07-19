N, K = map(int, input().split())
A = list(map(int, input().split()))
k = {}
C = [-1]*(N)
ans = 1

for i in range(N):
    if C[i-1]+1 == N:
        break
    for l in range(C[i-1]+1, N):
        k[A[l]] = l
        if len(k) > K:
            k.pop(A[l])
            C[i] = l-1
            L = l-i
            ans = max(L, ans)
            p = k[A[i]]
            if p == i:
                k.pop(A[i])
            break
        elif l == N-1 and len(k) <= K:
            C[i] = l
            L = l-i+1
            ans = max(L, ans)
            break

print(ans)
