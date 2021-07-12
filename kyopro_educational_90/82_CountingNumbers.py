L, R = map(int, input().split())
l = len(str(L))
r = len(str(R))
ans = 0
mod = 10**9+7
L %= mod
R %= mod

L9 = int('9'*l)%mod
if l == r:
    L9 = R
ans += (L+L9)*(L9-L+1)//2*l%mod

R10 = int('1'+'0'*(r-1))%mod
if l < r:
    ans += (R10+R)*(R-R10+1)//2*r
    ans %= mod

if l < r-1:
    for i in range(l+1, r):
        L9 = int('9'*(i))%mod
        R10 = int('1'+'0'*(i-1))%mod
        ans += (R10+L9)*(L9-R10+1)//2*i
        ans %= mod
print(ans)
