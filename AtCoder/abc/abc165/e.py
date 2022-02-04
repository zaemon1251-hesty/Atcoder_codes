N, M = map(int, input().split())
if M == 1:
    print(1, 2)
    exit()

ans = []
l, r = 1, M + 2

for diff in range(M, 0, -1):
    print(l, l + diff)
    l += 1
    l, r = r, l
