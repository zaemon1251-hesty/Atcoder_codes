def main():
    A, B = map(int, input().split())
    if (A + B) % 2 != 0:
        print("IMPOSSIBLE")
    else:
        print((A + B) // 2)


if __name__ == "__main__":
    main()
