def main():
    N, X = map(int, input().split())
    S = [i for i in range(1, N + 1) if i != X]
    n = len(S)
    L, R = S[: n // 2], S[n // 2 :]
    R = R[::-1]

    ans = []
    ans.append(X)
    if len(L) < len(R):
        ans.append(R.pop())

    dst = L if not (N % 2 == 0 and (X == N // 2 + 1)) else R
    while dst:
        ans.append(dst.pop())
        dst = R if dst is L else L

    print(*ans)


if __name__ == "__main__":
    main()
