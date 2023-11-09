def main():
    N = int(input())
    A = list(map(lambda x: int(x) - 1, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i, a in enumerate(A):
        if i != 0 and A[i] == A[i - 1] + 1:
            ans += C[A[i - 1]]
        ans += B[a]
    print(ans)


if __name__ == "__main__":
    main()
