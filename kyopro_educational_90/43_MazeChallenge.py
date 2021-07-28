from collections import deque
H, W = map(int, input().split())
sh, sw = map(int, input().split())
gh, gw = map(int, input().split())
sh, sw, gh, gw = sh-1, sw-1, gh-1, gw-1

field = [list(input()) for h in range(H)]

def convert(h,w,d):
    x = (W*h+w)*4+d
    return x

inf = float('inf')
turn = [inf]*convert(H-1,W-1,4)

dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]
q = deque()

for d in range(4):
    q.append([sh, sw, d, 0])

for d in range(4):
    turn[convert(sh, sw, d)] = 0

while q:
    ch, cw, cd, ct = q.popleft() #cd: current direction, ct: number of turns
    for nd in range(4): #nd: next direction
        #if nd == (cd+2)%4: continue #do not go back
        nh, nw = ch + dh[nd], cw + dw[nd]
        if 0 <= nh < H and 0 <= nw < W and field[nh][nw] != '#':
            nt = turn[convert(nh, nw, nd)]
            if cd == nd:
                if nt > ct:
                    nt = ct
                    turn[convert(nh, nw, nd)] = nt
                    q.appendleft([nh, nw, nd, nt])
            else:
                if nt > ct+1:
                    nt = ct+1
                    turn[convert(nh, nw, nd)] = nt
                    q.append([nh, nw, nd, nt])

ans = inf
for d in range(4):
    if turn[convert(gh, gw, d)] != -1:
        ans = min(ans, turn[convert(gh, gw, d)])
print(ans)
