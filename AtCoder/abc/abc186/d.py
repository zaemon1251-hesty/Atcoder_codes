def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N-1):
        ans += A[i] * (N-1-i)
    for j in range(1,N):
        ans -= A[j]*j
    print(ans)


if __name__ == '__main__':
    main()