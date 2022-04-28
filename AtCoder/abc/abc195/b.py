def main():
    A, B, W = map(int, input().split())
    W *= 1000
    s1 = (W + B - 1) // B
    s2 = W // A
    if s1 <= s2:
        print(s1, s2)
    else:
        print("UNSATISFIABLE")


if __name__ == '__main__':
    main()
