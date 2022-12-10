s = 0
S = input()
for i in S:
    s += int(i)
    s %= 9
print("Yes" if s == 0 else "No")
