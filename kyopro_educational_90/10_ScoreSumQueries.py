N = int(input())
s_1 = 0
s_2 = 0
S_1 = [0]
S_2 = [0]
for i in range(1, N+1):
    C, P = list(map(int, input().split()))
    C = C-1
    S_1.append(S_1[-1] + P*(1^C))
    S_2.append(S_2[-1] + P*C)
Q = int(input())
LR = [map(int, input().split()) for j in range(Q)]
L, R = [list(i) for i in zip(*LR)]
for j in range(Q):
    print(S_1[R[j]]-S_1[L[j]-1], S_2[R[j]]-S_2[L[j]-1])
