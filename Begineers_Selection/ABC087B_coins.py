A=int(input())
B=int(input())
C=int(input())
X=int(input())
a=500
b=100
c=50
Y=[]
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            Y.append(a*i+b*j+c*k)
print(Y.count(X))
