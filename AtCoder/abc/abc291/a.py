import sys
from string import ascii_uppercase


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    s = input()
    n = len(s)
    for i in range(n):
        if s[i] in ascii_uppercase:
            print(i + 1)
            return
    


if __name__ == '__main__':
    main()
