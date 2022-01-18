L, R = map(int, input().split())
S = list(input())
L -= 1
A = S[:L] + S[L:R][::-1] + S[R:]
print("".join(A))
