N = int(input())
X = list(map(int, input().split()))
X = sorted(X, reverse=True)
A = X[0]
B = X[1]
C = X[2]
for n in range(N//A, N//C+1):
    for x in range(N+1):
        p = N-C*n-(A-C)*x
        if p%(B-C) == 0:
            y = p//(B-C)
            z = n-y-x
            if 0 <= y <= n and 0 <= z <= n:
                n = x + y + z
                print(n)
                exit()
