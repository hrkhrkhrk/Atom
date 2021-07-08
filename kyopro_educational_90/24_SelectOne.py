N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
x = 0
for i in range(N):
    x += abs(B[i]-A[i])
if (K-x)%2 == 0 and (K-x) >= 0:
    print('Yes')
else:
    print('No')
