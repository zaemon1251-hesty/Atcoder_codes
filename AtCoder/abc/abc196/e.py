N = int(input())
low = -1 << 60
high = 1 << 60
add = 0
for i in range(N):
    A, T = map(int, input().split())
    if T == 1:
        low += A
        high += A
        add += A
    elif T == 2:
        if low < A:
            low = A
        if high < A:
            high = A
    else:
        if low > A:
            low = A
        if high > A:
            high = A
input()
for x in map(int, input().split()):
    print(min(high, max(low, x + add)))
