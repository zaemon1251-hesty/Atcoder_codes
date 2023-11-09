N = int(input())
(*S,) = map(int, input().split())

X = [0, 0]
for s in S:
    X.append(s - X[-1] - X[-2])

c1 = -min(X[::3])
c2 = -min(X[1::3])
c3 = min(X[2::3])
if c1 + c2 > c3:
    print("No")
else:
    print("Yes")
    op = [c1, c2, -c1 - c2]
    A = [x + op[i % 3] for i, x in enumerate(X)]
    print(*A)
