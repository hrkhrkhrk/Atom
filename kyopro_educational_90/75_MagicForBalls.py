def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N = int(input())
list = prime_factorize(N)
n = len(list)
n_2 = bin(n)[2:]
p = '1' + '0'*(len(n_2)-1)
if n_2 == p:
    print(len(n_2)-1)
else:
    print(len(n_2))
