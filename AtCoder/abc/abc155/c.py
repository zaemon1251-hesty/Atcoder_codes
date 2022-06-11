from collections import Counter


def main():
    N = int(input())
    S = Counter(input() for _ in range(N))
    ma = max(S.values())
    ans = []
    for k, v in S.items():
        if v == ma:
            ans.append(k)
    print(*sorted(ans), sep="\n")


if __name__ == '__main__':
    main()
