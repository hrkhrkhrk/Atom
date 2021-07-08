H, W = map(int, input().split())
A = [list(map(int, input().split())) for a in range(H)]
B = [[0]*W for i in range(H)]
H_sum = [sum(A[i]) for i in range(H)]
W_sum = [0]*W
for j in range(W):
    for i in range(H):
        W_sum[j] += A[i][j]
for i in range(H):
    for j in range(W):
        B[i][j] += W_sum[j] + H_sum[i] - A[i][j]
for i in range(H):
    print(*B[i])
