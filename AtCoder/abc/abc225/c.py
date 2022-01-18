ok = True
n, m = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(n)]
def dev(n):
    if n % 7 == 0:
        return 7
    else:
        return n % 7
for i in range(n):
    for j in range(1, m):
        if dev(B[i][j]) - dev(B[i][j-1]) != 1:
            ok = False
for j in range(m):
    for i in range(1, n):
        if B[i][j] - B[i-1][j] != 7:
            ok = False
print('Yes' if ok else 'No')
return 0
