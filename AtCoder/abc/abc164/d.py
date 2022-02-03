*S, = input()
A = [0] * 2019
ans = 0
p = 0
A[0] = 1
ti = 1
for i in range(len(S))[::-1]:
    p = int(S[i]) * ti + p
    p %= 2019
    A[p] += 1
    ti *= 10
    ti %= 2019
for i in range(2019):
    ans += A[i] * (A[i] - 1) // 2
print(ans)
