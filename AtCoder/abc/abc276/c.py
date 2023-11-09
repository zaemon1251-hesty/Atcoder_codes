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
    P = li()
    src = ".".join(map(lambda x: "%03d" % x, P))
    ans_array = [src]
    for i in range(N - 1):
        if P[i] == 1:
            continue
        Q = P.copy()

        try:
            supQi = max([q for q in Q[i + 1 :] if q < Q[i]])
        except ValueError:
            continue

        j = Q.index(supQi)

        Q[i], Q[j] = Q[j], Q[i]
        Q[i + 1 :] = sorted(Q[i + 1 :], reverse=True)
        ans_array.append(".".join(map(lambda x: "%03d" % x, Q)))

    ans_array.sort()
    i = ans_array.index(src)
    print(*map(int, ans_array[i - 1].split(".")))


if __name__ == "__main__":
    main()
