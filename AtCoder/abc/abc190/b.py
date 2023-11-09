def main():
    N, S, D = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    for x, y in A:
        if x < S and y > D:
            print("Yes")
            exit()
    print("No")


if __name__ == "__main__":
    main()
