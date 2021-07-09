import math
T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
for i in range(Q):
    E = int(input())
    y = -L/2*math.sin(2*E/T*math.pi)
    z = L/2*(1-math.cos(2*E/T*math.pi))
    if z == 0:
        arg = math.degrees(0)
    else:
        arg = math.degrees(math.atan(z/((X**2+(Y-y)**2)**(1/2))))
    print(arg)
