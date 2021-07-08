N = int(input())
for i in range(2**N):
    x = str(bin(i))
    x = x[2:]
    x = '0'*(N-len(x)) + x
    x_0 = 0
    x_1 = 0
    for j in range(N):
        if not x.count('0') == x.count('1'):
            break
        x_0 += 1^int(x[j])
        x_1 += int(x[j])
        if x_0 < x_1:
            break
        elif x_0 >= x_1 and j == N-1:
            X = x.replace('0', '(')
            X = X.replace('1', ')')
            print(X)
