A = list(input())
N = len(A)
ans = -1 << 18
for i in range(1 << N):
    x = []
    y = []
    for j in range(N):
        if (i >> j) & 1:
            x.append(A[j])
        else:
            y.append(A[j])
    try:
        x = sorted(x, reverse=True)
        y = sorted(y, reverse=True)
        x = int("".join(x))
        y = int("".join(y))
    except:
        x, y = 0, 0
    ans = max(ans, x * y)
print(ans)
