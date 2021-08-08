X = [0]*10**5

for i in range(10**5):
    x_str = str(i)
    y = 0
    for j in range(len(x_str)):
        y += int(x_str[j])
    X[i] = (i+y)%10**5

N, K = map(int, input().split())
vis = [[0]*2 for _ in range(10**5)]
x = N
for i in range(K):
    if vis[x][0] == 1:
        ls = vis[x][1]
        le = i
        break
    vis[x][0], vis[x][1] = 1, i
    x = X[x]
    if i == K-1:
        print(x)
        exit()
ll = le-ls

for i in range((K-ls)%ll):
    x = X[x]
print(x)
