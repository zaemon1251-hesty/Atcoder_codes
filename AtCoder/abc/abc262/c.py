def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    eqs = 0
    for i in range(1, N + 1):
        if i == A[i]:
            eqs += 1
    ans = eqs * (eqs - 1) // 2

    for i in range(1, N + 1):
        if i != A[i]:
            j = A[i]
            ans += int(j > i and A[j] == i)
    print(ans)


if __name__ == "__main__":
    main()
