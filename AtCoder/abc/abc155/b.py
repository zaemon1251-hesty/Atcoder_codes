def main():
    N = int(input())
    A = list(map(int, input().split()))
    print("APPROVED" if all(a % 6 == 0 or a % 10 == 0 or a % 2 != 0 for a in A) else "DENIED")


if __name__ == "__main__":
    main()
