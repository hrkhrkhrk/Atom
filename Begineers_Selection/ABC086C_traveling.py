N = int(input())
txy = [map(int, input().split()) for _ in range(N)]
t, x, y = [list(i) for i in zip(*txy)]
t.insert(0,0)
x.insert(0,0)
y.insert(0,0)
for i in range(1,N+1):
    opt=sum([abs(x[i]-x[i-1]),abs(y[i]-y[i-1])])
    if (t[i]-t[i-1]-opt)%2==0 and (t[i]-t[i-1]-opt)>=0:
        continue
    else:
        print('No')
        exit()
print('Yes')
