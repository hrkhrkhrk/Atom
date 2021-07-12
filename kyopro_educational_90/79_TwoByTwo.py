H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
B = [list(map(int, input().split())) for i in range(H)]
cnt = 0
for i in range(H-1):
    for j in range(W-1):
        x = B[i][j]-A[i][j]
        if x != 0:
            A[i][j] += x
            A[i][j+1] += x
            A[i+1][j] += x
            A[i+1][j+1] += x
            cnt += abs(x)
if A == B:
    print('Yes')
    print(cnt)
else:
    print('No')
