def main():
    S = list(input())
    f = "atcoder"
    A = list(map(lambda x: f.index(x), S))
    ans = 0
    for i in range(6):
        for j in range(i + 1, 7):
            if A[i] > A[j]:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
