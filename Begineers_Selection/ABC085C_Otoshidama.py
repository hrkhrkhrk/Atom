N, Y=map(int,input().split())
a=10000
b=5000
c=1000
x=[]
if Y%c==0:
    for i in range(int(Y/a)+1):
        Y_a=Y-a*i
        for j in range(int(Y_a/b)+1):
            Y_b=Y_a-b*j
            k=int(Y_b/c)
            if sum([i,j,k])==N:
                x=[i,j,k]
                break
        else:
            continue
        break
    if x==[]:
        print(*[-1,-1,-1])
    else:
        print(*x)
else:
    print(*[-1,-1,-1])
