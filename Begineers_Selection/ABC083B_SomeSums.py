N,A,B=map(int,input().split())
l_n=list(range(1,N+1))
l_n_str = [str(n) for n in l_n]
X=[]
for n in range(1,N+1):
    n_str=list(str(n))
    n_int=[int(m) for m in n_str]
    X.append(sum(n_int))
Y=[1 if A<=i<=B else 0 for i in X]
Z=[n*y for (n,y) in zip(l_n,Y)]
print(sum(Z))
