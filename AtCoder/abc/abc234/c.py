k = int(input())


def f(n):
    s = ""
    while n != 0:
        s += "2" if n % 2 == 0 else "0"
        n //= 2
    return s


print(f(k))
