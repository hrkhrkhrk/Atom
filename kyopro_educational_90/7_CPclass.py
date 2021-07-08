def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] <= value <= data[mid+1]:
            return mid
        elif data[mid+1] < value < data[-1]:
            left = mid + 1
        elif data[mid] > value > data[0]:
            right = mid - 1
        elif data[0] >= value:
            return 0
        else:
            return -1

N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())
for i in range(Q):
    B = int(input())
    if len(A) == 1:
        print(abs(A[0]-B))
    else:
        idx = binary_search(A, B)
        if idx == Q-1:
            print(abs(A[idx]-B))
        else:
            print(min(abs(A[idx]-B), abs(A[idx+1]-B)))
