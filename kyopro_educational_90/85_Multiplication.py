import bisect
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

K = int(input())
d = make_divisors(K)
ans = 0

for a in d:
    if a**3 <= K:
        d2 = make_divisors(K//a)
        idx = bisect.bisect_left(d2, a)
        ans += (len(d2)+1)//2-idx
print(ans)
