def main():
    N = int(input())
    ans = sum(len(str(i)) % 2 == 1 for i in range(1, N + 1))
    print(ans)


if __name__ == "__main__":
    main()
