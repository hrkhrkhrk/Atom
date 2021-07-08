Q = int(input())
from collections import deque
X = deque()
for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        X.appendleft(x)
    elif t == 2:
        X.append(x)
    else:
        print(X[x-1])
