n = int(input())
c = [int(i) for i in input().split()]

min_c, min_j = n + 1, 9
for j in range(8, -1, -1):
    if c[j] < min_c:
        min_c, min_j = c[j], j

max_k = n // min_c
cost = max_k * min_c

cnt = [0] * 9
for j in range(8, min_j, -1):
    while cost - min_c + c[j] <= n:
        cnt[j] += 1
        max_k -= 1
        cost += c[j] - min_c
cnt[min_j] = max_k

ans = ''
for j in range(8, min_j - 1, -1):
    ans += str(j + 1) * cnt[j]
print(ans)
