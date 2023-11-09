import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    _ = ii()
    A = li()
    odd, even = [], []
    for a in A:
        if a % 2 == 0:
            even.append(a)
        else:
            odd.append(a)
    odd.sort()
    even.sort()

    if len(odd) == len(even) == 1:
        print(-1)
        return

    ans = 0

    if len(even) >= 2:
        ans = max(ans, even[-1] + even[-2])

    if len(odd) >= 2:
        ans = max(ans, odd[-1] + odd[-2])

    print(ans)


if __name__ == "__main__":
    main()
