from heapq import heappop, heappush
Q = int(input())
B = []
num = 0
for _ in range(Q):
    d = input()
    if len(d) != 1:
        ty, x = map(int, d.split())
        if ty == 1:
            heappush(B, x-num)
        else:
            num += x
    else:
        p = heappop(B)
        print(p + num)
