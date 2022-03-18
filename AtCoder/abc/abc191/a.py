def main():
    v, t, s, d = map(int, input().split())
    if v * t <= d <= v * s:
        print("No")
        exit()
    print("Yes")


if __name__ == '__main__':
    main()
