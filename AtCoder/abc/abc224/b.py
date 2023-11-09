h, w = map(int, input().split())
S = []
for _ in range(h):
    S.append(list(map(int, input().split())))
for i1 in range(h - 1):
    for i2 in range(i1 + 1, h):
        for j1 in range(w - 1):
            for j2 in range(j1 + 1, w):
                if (S[i1][j1] + S[i2][j2]) > (S[i2][j1] + S[i1][j2]):
                    print("No")
                    exit()
print("Yes")
b()
