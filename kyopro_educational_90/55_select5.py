N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
x = 0
for i in range(N):
    for j in range(i):
        for k in range(j):
            for l in range(k):
                for m in range(l):
                    X = A[m] % P * A[l] % P * A[k] % P * A[j] % P * A[i] % P
                    if X == Q:
                        x += 1
print(x)
