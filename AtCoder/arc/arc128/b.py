ans = []
for _ in range(int(input())):
    r = list(map(int, input().split()))
    r.sort()
    if r[0] % 3 == r[1] % 3:
        ans.append(r[1])
    elif r[0] % 3 == r[2] % 3 or r[1] % 3 == r[2] % 3:
        ans.append(r[2])
    else:
        ans.append(-1)
print(*ans, sep="\n")
b()
