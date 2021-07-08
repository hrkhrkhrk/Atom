N=int(input())
A=list(map(int,input().split()))
Alice=[]
Bob=[]
A=sorted(A, reverse=True)
for i in range(N//2):
    Alice.append(A[2*i])
    Bob.append(A[2*i+1])
if N%2==1:
    Alice.append(A[N-1])
print('{}'.format(sum(Alice)-sum(Bob)))
