from math import sqrt


def main():
    N = int(input())
    A = list(map(lambda x: abs(int(x)), input().split()))
    m = sum(A)
    u = sqrt(sum(map(lambda x: x * x, A)))
    c = max(A)
    print(m, u, c, sep="\n")


if __name__ == "__main__":
    main()
