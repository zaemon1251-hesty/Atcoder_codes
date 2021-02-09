#拡張ユークリッドの互除法 a'gx+b'gy=gとなるx,y,gを求める（逆元を求める際にmodが素数じゃないとき）

# Euclidean Algorithm
def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n

# Euclidean Algorithm (non-recursive)
def gcd2(m, n):
    while n:
        m, n = n, m % n
    return m

# Extended Euclidean Algorithm
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

# lcm (least common multiple)
def lcm(m, n):
    return m//gcd(m, n)*n


if __name__ =="__main__":
    print(extgcd(10000,14))
    #print(gcd(10,3))