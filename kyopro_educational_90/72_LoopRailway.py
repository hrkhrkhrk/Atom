H, W = map(int, input().split())
field = [list(input()) for h in range(H)]

dist = [[-1]*W for h in range(H)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, cnt):
    if dist[x][y] != -1:
        if cnt - dist[x][y] > 2:
            return cnt - dist[x][y]
        else:
            return -1

    ans = -1
    dist[x][y] = cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and field[nx][ny] != '#':
            ans = max(ans, dfs(nx, ny, cnt+1))

    dist[x][y] = -1
    return ans

ans = -1
for h in range(H):
    for w in range(W):
        if field[h][w] != '#':
            ans = max(ans, dfs(h, w, 0))
print(ans)
