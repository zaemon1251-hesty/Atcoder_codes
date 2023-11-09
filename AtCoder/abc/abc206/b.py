N = int(input())
ans = 0
i = 0
while True:
    if ans >= N:
        print(i)
        exit()
    i += 1
    ans += i
