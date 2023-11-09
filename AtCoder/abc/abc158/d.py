from collections import deque

S = deque(list(input()))
Q = int(input())
flg = 0
for _ in range(Q):
    ipt = input()
    if ipt[0] == "1":
        flg = 1 - flg
    else:
        _, f, c = map(str, ipt.split())
        f = int(f) - 1
        if (f ^ flg) & 1:
            S.append(c)
        else:
            S.appendleft(c)
if flg == 1:
    S.reverse()
print("".join(list(S)))
