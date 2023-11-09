def main():
    A = list(map(int, input().split()))
    print("Yes" if any(sum(A) == 3 * a for a in A) else "No")


if __name__ == "__main__":
    main()
