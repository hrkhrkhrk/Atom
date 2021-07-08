S=input()
T=[]
a='dream'
b='dreamer'
c='erase'
d='eraser'
import re
while d in S:
    S=(re.sub(d, '', S))
while c in S:
    S=(re.sub(c, '', S))
while b in S:
    S=(re.sub(b, '', S))
while a in S:
    S=(re.sub(a, '', S))
if S=='':
    print('YES')
else:
    print('NO')
