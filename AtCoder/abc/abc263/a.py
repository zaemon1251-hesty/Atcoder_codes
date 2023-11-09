from collections import Counter


def main():
    A = Counter(map(int, input().split()))
    print("Yes" if (len(list(A.values())) == 2 and list(A.values())[0] in [2, 3]) else "No")


if __name__ == "__main__":
    main()
