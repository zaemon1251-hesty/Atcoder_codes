def main():
    N = int(input())
    A = list(map(int, input().split()))
    bucket = [0] * 200100
    for a in A:
        bucket[a] += 1
    ans = N * (N - 1) * (N - 2) // 6
    for b in bucket:
        ans -= b * (b - 1) * (b - 2) // 6
        ans -= (N - b) * b * (b - 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
