H, W = map(int, input().split())
G = []


def fx(x):
    if x == "-":
        return -1
    else:
        return 1


for i in range(H):
    f = list(map(fx, list(input())))
    G.append(f)
opt = [[0] * (W) for _ in range(H)]


def operation(i, j):
    if i == H - 1 and j == W - 1:
        return 0
    elif i == H - 1:
        return opt[i][j + 1] + G[i][j + 1] if (i + j) % 2 == 0 else opt[i][j + 1] - G[i][j + 1]
    elif j == W - 1:
        return opt[i + 1][j] + G[i + 1][j] if (i + j) % 2 == 0 else opt[i + 1][j] - G[i + 1][j]
    else:
        if (i + j) % 2 == 0:
            return max(opt[i][j + 1] + G[i][j + 1], opt[i + 1][j] + G[i + 1][j])
        else:
            return min(opt[i][j + 1] - G[i][j + 1], opt[i + 1][j] - G[i + 1][j])


for i in range(H - 1, -1, -1):
    for j in range(W - 1, -1, -1):
        opt[i][j] = operation(i, j)
if opt[0][0] > 0:
    print("Takahashi")
elif opt[0][0] < 0:
    print("Aoki")
else:
    print("Draw")
