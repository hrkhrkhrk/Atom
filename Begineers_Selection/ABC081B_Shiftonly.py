N=int(input())
A=list(map(int,input().split()))
j=-1
B=[0]*N
def div_2(n):
    return n/2
def mod_2(n):
    return n%2
while B==[0]*N:
    B = list(map(mod_2, A))
    A = list(map(div_2, A))
    j+=1
else:
    print(j)
