def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = sum(i * j for i, j in zip(A, B))
    print("Yes" if ans == 0 else "No")


if __name__ == "__main__":
    main()
