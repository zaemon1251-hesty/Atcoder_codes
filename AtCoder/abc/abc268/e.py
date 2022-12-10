def main():
    N = int(input())
    P = list(map(int, input().split()))
    ix, iv = [0] * (2 * N), [0] * (2 * N)
    for i in range(N):
        j = (i - P[i]) % N
        centre = j + N // 2 + 1

        iv[j] -= j
        iv[centre] += j
        ix[j] += 1
        ix[centre] -= 1

        iv[centre] += N + j
        iv[N + j] -= N + j
        ix[centre] -= 1
        ix[N + j] += 1

    for i in range(2 * N - 1):
        iv[i + 1] += iv[i]
        ix[i + 1] += ix[i]

    ans = 1 << 60
    for i in range(N):
        ans = min(ans, iv[i] + ix[i] * i + iv[i + N] + ix[i + N] * (i + N))

    print(ans)


if __name__ == '__main__':
    main()
