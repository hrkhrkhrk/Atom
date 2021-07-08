N=int(input())
D=[]
D=[int(input()) for i in range(N)]
j=0
while not D==[0]*N:
    D=[0 if i==max(D) else i for i in D]
    j+=1
print(j)
