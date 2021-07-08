N = int(input())
LC = {}
for i in range(1, N+1):
    S = input()
    if S not in LC.keys():
        print(i)
    LC[S] = i
