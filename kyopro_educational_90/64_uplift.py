N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = [0]*(N-1)
for i in range(N-1):
    X[i] = A[i+1]-A[i]
S = sum([abs(x) for x in X])
for i in range(Q):
    L, R, V = map(int, input().split())
    gap = 0
    if L > 1:
        left = X[L-2]
        X[L-2] += V
        gap += abs(X[L-2])-abs(left)
    if R < N:
        right = X[R-1]
        X[R-1] -= V
        gap += abs(X[R-1])-abs(right)
    S += gap
    print(S)
