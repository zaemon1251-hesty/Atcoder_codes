from bisect import bisect_left


def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A1 = []
    A2 = []
    for i in range(1 << (N // 2)):
        a1 = 0
        for j in range(N // 2):
            if (i >> j) & 1:
                a1 += A[j]
        A1.append(a1)
    A1.sort()
    for i in range(1 << (N - N // 2)):
        a2 = 0
        for j in range(N - N // 2):
            if (i >> j) & 1:
                a2 += A[j + N // 2]
        A2.append(a2)
    A2.sort()

    ans = 0
    for i in range(len(A1)):
        j = bisect_left(A2, T - A1[i])
        j = min(j, len(A2) - 1)
        if A1[i] + A2[j] <= T:
            ans = max(ans, A1[i] + A2[j])
        if j > 0 and A1[i] + A2[j - 1] <= T:
            ans = max(ans, A1[i] + A2[j - 1])

    print(ans)


if __name__ == "__main__":
    main()
