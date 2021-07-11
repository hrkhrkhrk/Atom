import bisect
N = int(input())
A = list(map(int, input().split()))
A = A + A
B = A
for i in range(1, 2*N):
    B[i] = B[i-1] + A[i]
for i in range(N):
    L = B[i]
    R = B[N-1]/10 + L
    idx = bisect.bisect(B, R)
    if B[idx-1] == R:
        print('Yes')
        exit()
print('No')
