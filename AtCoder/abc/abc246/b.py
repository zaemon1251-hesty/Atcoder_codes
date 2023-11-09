from math import sqrt


def main():
    A, B = map(int, input().split())
    R = sqrt(A**2 + B**2)
    print(A / R, B / R)


if __name__ == "__main__":
    main()
