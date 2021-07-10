from operator import mul
from functools import reduce
def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

N, L = map(int, input().split())
l = N%L
cnt = 0
for l in range(N//L+1):
    x = N-L*l
    cnt += combinations_count(x+l, x)
print(cnt%(10**9+7))
