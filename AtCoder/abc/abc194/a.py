def main():
    A, B = map(int, input().split())
    A += B
    ans = 4
    if A >= 15 and B >= 8:
        ans = 1
    elif A >= 10 and B >= 3:
        ans = 2
    elif A >= 3:
        ans = 3
    print(ans)


if __name__ == "__main__":
    main()
