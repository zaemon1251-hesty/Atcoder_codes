def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans1 = 0
    ans2 = 0
    for i in range(N):
        ans1 += A[i] == B[i]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            ans2 += A[i] == B[j]
    print(ans1)
    print(ans2)


if __name__ == "__main__":
    main()
