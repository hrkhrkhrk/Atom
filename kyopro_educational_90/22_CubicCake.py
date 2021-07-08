L = list(map(int, input().split()))
import math
x = 0
for i in range(len(L)):
    x = math.gcd(x, L[i])
C = 0
for i in range(len(L)):
    C += L[i]//x-1
print(C)
