def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = []
    for i in range(N):
        if A[i] != X:
            ans.append(A[i])
    print(*ans)


if __name__ == "__main__":
    main()
