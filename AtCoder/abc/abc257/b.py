def main():
    N, K, Q = map(int, input().split())
    mas = [0] * N
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    for i, a in enumerate(A):
        mas[a - 1] = i + 1

    for ll in L:
        d = mas.index(ll)
        if d == N - 1:
            continue
        else:
            if mas[d + 1] == 0:
                mas[d + 1], mas[d] = mas[d], mas[d + 1]

    ans = [0] * K
    for i in range(N):
        if mas[i] != 0:
            ans[mas[i] - 1] = i + 1

    print(*ans)


if __name__ == '__main__':
    main()
