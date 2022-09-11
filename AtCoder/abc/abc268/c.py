def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        dst = (i - P[i]) % N
        ans[dst] += 1
        ans[(dst + 1) % N] += 1
        ans[(dst - 1) % N] += 1
    print(max(ans))


if __name__ == '__main__':
    main()
