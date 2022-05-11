from collections import Counter


def main():
    n = int(input())
    A = Counter(map(int, input().split()))
    B = list(map(int, input().split()))
    C = Counter(map(lambda x: int(x) - 1, input().split()))
    ans = 0
    for k, v in C.items():
        val = B[k]
        ans += v * A[val]
    print(ans)


if __name__ == "__main__":
    main()
