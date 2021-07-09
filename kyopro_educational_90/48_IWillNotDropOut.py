N, K = map(int, input().split())
AB= [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]
C = [0]*N
for i in range(N):
    C[i] = A[i]-B[i]
X = sorted(B+C, reverse = True)
print(sum(X[:K]))
