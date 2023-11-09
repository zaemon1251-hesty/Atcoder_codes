S = input()
se = set()
flg = True
lg = False
sm = False
for s in S:
    if s in se:
        flg = False
    se.add(s)
    if s == s.lower():
        sm = True
    else:
        lg = True
print("Yes" if (flg and lg and sm) else "No")
