N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
A.append(L)
B = [0]*(N+1)
B[0] = A[0]
for i in range(1, N+1):
    B[i] = A[i]-A[i-1]

l = 0
r = L//(K+1)
s = r
while l < r-1:
    part = 0
    x = []
    for i in range(0, N+1):
        part += B[i]
        if part >= s:
            x.append(part)
            part = 0
            if len(x) == K+1:
                ans = s
                l = s
                break
        if i == N:
            r = s
            break
    s = ((l+r)+1)//2
print(ans)
