def maina():
    n = int(input())
    a = list(map(int, input().split()))

    ans = [0]*n

    for i in range(n-1):
        if a[i] > a[i+1]:
            ans[i] ^= 1
            ans[i+1] ^= 1

    print(*ans)


def mainb():
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
    print(*ans, sep='\n')


mainb()
