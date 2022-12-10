def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]

    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    for hi in range(1 << H1):
        if bin(hi).count("1") != H2:
            continue
        for wi in range(1 << W1):
            if bin(wi).count("1") != W2:
                continue

            hs = [hj for hj in range(H1) if hi >> hj & 1]
            ws = [wj for wj in range(W1) if wi >> wj & 1]

            flg = True
            for i, x in enumerate(hs):
                for j, y in enumerate(ws):
                    if B[i][j] != A[x][y]:
                        flg = False
                        break
                else:
                    continue
                break

            if flg:
                print("Yes")
                exit()

    print("No")


if __name__ == '__main__':
    main()
