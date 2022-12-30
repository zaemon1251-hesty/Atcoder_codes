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
    s = list(input())
    cnt = 0
    while s:
        if len(s) > 1 and s[-1] == s[-2] == "0":
            cnt += 1
            s.pop()
            s.pop()
        else:
            cnt += 1
            s.pop()
    print(cnt)


if __name__ == '__main__':
    main()
