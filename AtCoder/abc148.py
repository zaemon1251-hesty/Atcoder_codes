
def mainc():
    from math import gcd
    a, b = map(int, input().split())
    print(a*b//gcd(a, b))
    pass


def maind():
    N = int(input())
    A = list(map(int, input().split()))
    sp = 0
    for i in range(N):
        if A[i] == sp + 1:
            sp += 1
    print(N - sp if sp != 0 else -1)


def maine():
    n = int(input())
    if n % 2 != 0:
        print(0)
        exit()
    i = 10
    devide = []
    while n // i > 0:
        devide.append(n // i)
        i *= 5
    print(sum(devide))


if __name__ == "__main__":
    maind()
