N, Q = map(int, input().split())
A = list(map(int, input().split()))
t = 0
for i in range(Q):
    T, x, y = map(int, input().split())
    if T == 1:
        A[x-1-t], A[y-1-t] = A[y-1-t], A[x-1-t]
    elif T == 2:
        t += 1
        t = t%N
    else:
        print(A[x-1-t])
