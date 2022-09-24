import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N = ii()
    S = [li() for _ in range(N)]
    S.sort(key=lambda x: (x[1], x[0]))

    now = 0
    for i in range(N):
        a, b = S[i]
        if now + a <= b:
            now += a
            continue
        print("No")
        exit()
    print("Yes")


if __name__ == '__main__':
    main()
