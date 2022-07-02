def main():
    N = int(input())
    a, b = N // 60, N % 60
    a += 21
    if b < 10:
        b = str(0) + str(b)
    print(f"{a}:{b}")


if __name__ == '__main__':
    main()
