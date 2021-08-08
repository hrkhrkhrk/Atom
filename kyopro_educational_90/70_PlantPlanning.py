N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

X = sorted(X)
Y = sorted(Y)

a, b = X[N//2], Y[N//2]
ans_a, ans_b = 0, 0
for i in range(N):
    ans_a += abs(X[i]-a)
    ans_b += abs(Y[i]-b)

print(ans_a+ans_b)
