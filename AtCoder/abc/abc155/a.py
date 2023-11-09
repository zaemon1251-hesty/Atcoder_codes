def main():
    A = list(map(int, input().split()))
    print("Yes" if len(set(A)) == 2 else "No")


if __name__ == "__main__":
    main()
