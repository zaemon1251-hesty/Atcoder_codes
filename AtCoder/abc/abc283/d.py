import sys
from collections import defaultdict


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

    bag = defaultdict(set)
    stack = []

    stack = []
    used = set()
    for i in range(n):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            for a in bag[len(stack)]:
                if a in used:
                    used.remove(a)
            stack.pop()
        elif s[i] not in used:
            bag[len(stack)].add(s[i])
            used.add(s[i])
        else:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    main()
