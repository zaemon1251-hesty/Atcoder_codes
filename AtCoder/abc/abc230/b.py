<<<<<<< HEAD
def main():
    S = input()
    T = "oxx" * 10**3
    if S in T:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
=======
N, D = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
S.sort(key=lambda x: (x[1]))
removed = -1
ans = 0
for a, b in S:
    # a が removed より大きい = まだ取り除いてない
    if a > removed:
        removed = b + D - 1
        ans += 1
print(ans)
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
