def main():
    X, Y = map(int, input().split("."))
    res = "-" if Y <= 2 else "" if Y <= 6 else "+"
    print(str(X) + res)


if __name__ == "__main__":
    main()
