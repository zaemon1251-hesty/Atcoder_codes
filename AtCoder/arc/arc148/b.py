def main():
    def f(T):
        U = [c for c in reversed(T)]
        for i in range(len(U)):
            U[i] = 'd' if U[i] == 'p' else 'p'
        return "".join(U)

    N = int(input())
    S = input()
    L = 0
    while L != N and S[L] == 'd':
        L += 1
    ans = S
    for R in range(L + 1, N + 1):
        ans = min(ans, S[:L] + f(S[L:R]) + S[R:])
    print(ans)


if __name__ == '__main__':
    main()
