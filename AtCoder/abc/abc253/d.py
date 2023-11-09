from math import gcd


def cusum(x: int):
    return x * (x + 1) // 2


def main():
    N, A, B = map(int, input().split())
    AB = A * B // gcd(A, B)
    p = N // A
    q = N // B

    pq = N // AB
    print(cusum(N) - A * cusum(p) - B * cusum(q) + AB * cusum(pq))


if __name__ == "__main__":
    main()
