def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    ans_set = set()
    for i in range(N):
        s = A[i]
        if s <= W:
            ans_set.add(s)

    for i in range(N - 1):
        for j in range(i + 1, N):
            s = A[i] + A[j]
            if s <= W:
                ans_set.add(s)

    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                s = A[i] + A[j] + A[k]
                if s <= W:
                    ans_set.add(s)
    print(len(ans_set))


if __name__ == "__main__":
    main()
