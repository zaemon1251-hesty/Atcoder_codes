from collections import Counter


def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = Counter(A)
    ans = 0
    for i, v in S.items():
        for j, u in S.items():
            if i == j:
                continue
            else:
                ans += v * u * (i - j) ** 2
    print(ans // 2)


if __name__ == "__main__":
    main()
