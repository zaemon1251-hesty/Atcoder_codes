INF = 10**18 + 1
D = 5


def calc(bit, b):
    ret = 0
    v = 1
    for i in range(D):
        if bit >> i & 1:
            ret += v
        if v <= INF / b:
            v *= b
        else:
            v = INF
    return ret


def solve(N):
    ans = 0

    b = 2
    while b**D <= N:
        x = N
        flag = True
        while x:
            if x % b > 1:
                flag = False
                break
            x //= b
        if flag:
            ans += 1
        b += 1

    for bit in range(1, 1 << D):
        ok = 2
        ng = N + 1
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if calc(bit, mid) <= N:
                ok = mid
            else:
                ng = mid
        if calc(bit, ok) == N:
            ans += 1

    return ans


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        ans = solve(N)
        print(ans)


main()
