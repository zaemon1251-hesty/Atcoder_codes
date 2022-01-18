N = int(input())
A = []
X = []
Y = []
for _ in range(N):
    a = int(input())
    t_x = []
    t_y = []
    for t in range(a):
        x, y = map(int, input().split())
        x -= 1
        t_x.append(x)
        t_y.append(y)
    X.append(t_x)
    Y.append(t_y)
    A.append(a)
ans = 0
for i in range(1 << N):
    hon = [0]*N
    for j in range(N):
        if (i >> j) & 1:
            hon[j] = 1
    if check(N, hon, X, Y):
        ans = max(ans, sum(hon))
print(ans)
