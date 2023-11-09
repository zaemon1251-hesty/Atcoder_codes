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

    N, X = mi()
    L = li()
    D = [0]
    for Li in L:
        D.append(D[-1] + Li)
    print(sum(d <= X for d in D))


if __name__ == "__main__":
    main()
