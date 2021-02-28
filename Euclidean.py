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

def mod(a,b):
  return (a%b+b)%b

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

#中国剰余定理（t ≡ b1 (mod m1), t ≡ b2 (mod m2)　となる最小のtを求める）
def crt(b,m):
    d, x, _ = extgcd(m[0],m[1])
    if (b[1] - b[0])%d != 0:return (0, -1)
    lm = lcm(m[0],m[1])
    tmp = (b[1] - b[0]) // d * x % (m[1]//d)
    r = (b[0] + m[0] * tmp) % m
    return (r, lm)


if __name__ =="__main__":
    print(extgcd(10000,14))#(2,-3,2143) -> 10000*-3 + 14*2143 = 2(=gcd(10000,14))
    print(extgcd(4,-4))
    