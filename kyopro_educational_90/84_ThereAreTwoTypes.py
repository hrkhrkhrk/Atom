import bisect
N = int(input())
S = input()
X = [[], []]
cnt = 0
for i in range(N):
    if S[i] == 'o':
        X[0].append(i)
    else:
        X[1].append(i)
if X[0] == [] or X[1] == []:
    print(0)
    exit()
for j in range(2):
    for i in range(len(X[j])):
        x = bisect.bisect(X[1^j], X[j][i])
        if x < len(X[1^j]):
            y = len(S)-X[1^j][x]
            cnt += y
print(cnt)
