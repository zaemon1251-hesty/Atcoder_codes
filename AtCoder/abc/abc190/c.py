n, m = map(int, input().split())
a = []
b = []
for _ in range(m):
    a1, b1 = map(int, input().split())
    a.append(a1 - 1)
    b.append(b1 - 1)

k = int(input())
bow = []
maxc = 0
for _ in range(k):
    c1, d1 = map(int, input().split())
    bow.append([c1 - 1, d1 - 1])

for i in range(2**k):
    dish = [0] * n
    for j in range(k):
        if (i >> j) & 1:  # 順に右にシフトさせ最下位bitのチェックを行う
            dish[bow[j][1]] += 1

        else:
            dish[bow[j][0]] += 1
    count = 0
    for i in range(m):
        if dish[a[i]] >= 1 and dish[b[i]] >= 1:
            count += 1
    maxc = max(maxc, count)

print(maxc)
