import collections
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A = collections.Counter(sorted([i%46 for i in A]))
B = collections.Counter(sorted([i%46 for i in B]))
C = collections.Counter(sorted([i%46 for i in C]))
a = list(A.keys())
b = list(B.keys())
c = list(C.keys())
a_n = list(A.values())
b_n = list(B.values())
c_n = list(C.values())

cnt = 0
for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(C)):
            if (a[i]+b[j]+c[k])%46 == 0:
                cnt += a_n[i]*b_n[j]*c_n[k]
print(cnt)
