n, m = map(int, input().split())
a = list(map(int, input().split()))

x = [[] for i in range(n)]
for i, ai in enumerate(a):
    x[ai].append(i)


def check(y):
    if len(y) == 0:
        return True
    if y[0] >= m or y[-1] < n - m:
        return True
    for j in range(1, len(y)):
        if y[j] - y[j - 1] > m:
            return True
    return False


for i in range(n):
    if check(x[i]):
        print(i)
        exit()
print(n)
