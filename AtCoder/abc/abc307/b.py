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

    N = ii()
    S = [input() for _ in range(N)]
    ij = [(i, j) for i in range(N) for j in range(N) if i != j]
    for i, j in ij:
        tmp = S[i] + S[j]
        length = len(tmp)
        for k in range(length // 2):
            if tmp[k] != tmp[length - k - 1]:
                break
        else:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
