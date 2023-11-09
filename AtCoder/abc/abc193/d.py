from collections import Counter


def f(d):
    res = 0
    for k, v in enumerate(d):
        res += (k + 1) * 10**v
    return res


def make_bucket(a):
    res = [0] * 9
    for item in a:
        res[int(item) - 1] += 1
    return res


def main():
    K = int(input())
    S = make_bucket(list(input())[:-1])
    T = make_bucket(list(input())[:-1])
    rst = [K] * 9
    ans = 0
    for deck in [S, T]:
        for k, v in enumerate(deck):
            rst[k] -= v
    total = sum(rst) * (sum(rst) - 1)
    for tkhs in range(9):
        for aok in range(9):
            if tkhs == aok:
                if rst[tkhs] < 2:
                    continue
                match = rst[tkhs] * (rst[tkhs] - 1)
            else:
                if rst[tkhs] < 1 or rst[aok] < 1:
                    continue
                match = rst[tkhs] * rst[aok]
            S[tkhs] += 1
            T[aok] += 1
            if f(S) > f(T):
                ans += match
            S[tkhs] -= 1
            T[aok] -= 1
    print(ans / total)


if __name__ == "__main__":
    main()
