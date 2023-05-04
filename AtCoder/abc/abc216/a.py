<<<<<<< HEAD
def main():
    X, Y = map(int, input().split("."))
    res = "-" if Y <= 2 else "" if Y <= 6 else "+"
    print(str(X) + res)


if __name__ == '__main__':
    main()
=======
N = int(input())
ans = ""
while N > 0:
    if N % 2 == 0:
        N //= 2
        ans += "B"
    else:
        N -= 1
        ans += "A"
print("".join(list(ans)[::-1]))
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
