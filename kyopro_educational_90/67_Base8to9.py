def base_n10(n_b, b):
    n = 0
    l = len(n_b)
    for i in range(l):
        n += b**(l-i-1)*int(n_b[i])
    return n
def base_10n(n, b):
    if n//b:
        return base_10n(n//b, b) + str(n%b)
    return str(n%b)

N, K = map(int, input().split())
N8 = str(N)
for i in range(K):
    N10 = base_n10(N8, 8)
    N9 = base_10n(N10, 9)
    N8 = N9.replace('8', '5')
print(N8)
