import collections
H, W = map(int, input().split())
P = []
for h in range(H):
    p = list(map(int, input().split()))
    P.append(p)
ans = 1
for bit in range(1<<H):
    w_idx = []
    hg = 0
    for h in range(H):
        if (bit>>h)&1:
            hg += 1

    for w in range(W):
        q = []
        for h in range(H):
            if (bit>>h)&1:
                q.append(P[h][w])
                if q[0] != P[h][w]:
                    break
            if q != [] and h == H-1:
                w_idx.append(q[0])

    if w_idx != []:
        w_idx = collections.Counter(w_idx)
        wg = w_idx.most_common()[0][1]
        ans = max(ans, wg*hg)

print(ans)
