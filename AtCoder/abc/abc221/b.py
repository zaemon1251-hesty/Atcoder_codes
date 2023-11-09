s = input()
t = input()
cnt = []
for i in range(len(s)):
    if s[i] != t[i]:
        cnt.append((s[i], t[i], i))
if len(cnt) == 2:
    a, b = cnt[0], cnt[1]
    if a[0] == b[1] and a[1] == b[0] and abs(a[2] - b[2]) == 1:
        cnt = []
print("Yes" if len(cnt) == 0 else "No")
