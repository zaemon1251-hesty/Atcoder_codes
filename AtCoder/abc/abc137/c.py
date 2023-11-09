from collections import Counter


def main():
    N = int(input())
    C = ["".join(sorted(input())) for _ in range(N)]
    S = Counter(C)
    ans = 0
    for k, v in S.items():
        ans += v * (v - 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
