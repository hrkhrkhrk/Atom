import queue
N = int(input())
X  = [[] for i in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())
    X[A-1].append(B-1)
    X[B-1].append(A-1)

def distance(N, s, X):
    d = [-1]*N
    d[s] = 0
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        t = q.get()
        for i in X[t]:
            if d[i] == -1:
                d[i] = d[t]+1
                q.put(i)
    return d

d_0 = distance(N, 0, X)
idx = d_0.index(max(d_0))
d_i = distance(N, idx, X)
print(max(d_i)+1)
