s, t, x = map(int, input().split())
if t < s:
    t += 24
for i in range(s, t):
    if x % 24 == i % 24:
        print("Yes")
        exit()
print("No")
