def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    recieved = T
    for i in range(3 * N):
        recieved[i % N] = min(
            recieved[i % N],
            recieved[(i - 1) % N] + S[(i - 1) % N]
        )
    print(*recieved, sep="\n")


if __name__ == '__main__':
    main()
