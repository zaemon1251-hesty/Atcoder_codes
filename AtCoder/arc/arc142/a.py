def main():
    N, K = map(int, input().split())
    if K % 10 == 0:
        if N < K:
            print(0)
        else:
            print(1)
    else:
        revK = int(str(K)[::-1])
        ans = 0

        if revK < K:
            print(0)
            exit()

        if revK != K:
            while revK <= N:
                ans += 1
                revK *= 10

        while K <= N:
            ans += 1
            K *= 10
        print(ans)


if __name__ == '__main__':
    main()
