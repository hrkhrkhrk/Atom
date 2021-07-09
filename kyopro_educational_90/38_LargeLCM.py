import math
A, B = map(int, input().split())
if A > 10**18 or B > 10**18:
    print('Large')
    exit()
gcd = math.gcd(A, B)
ans = A*B//gcd
if ans > 10**18:
    print('Large')
    exit()
print(ans)
