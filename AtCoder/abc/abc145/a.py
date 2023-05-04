<<<<<<< HEAD
def main():
    r = int(input())
    print(r**2)


if __name__ == '__main__':
    main()
=======
mod = 10**9 + 7
X, Y = map(int, input().split())
z = X + Y
if (X + Y) % 3 != 0 or not (z//3 <= X <= 2*z//3):
    print(0)
    exit()
st = z//3
u = X - st
ans = 1
lazy = 1
for i in range(u):
    ans *= st - i
    lazy *= i + 1
    ans %= mod
    lazy %= mod
ans *= pow(lazy, mod - 2, mod)
print(ans % mod)
_name__ == "__main__":
maind()
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
