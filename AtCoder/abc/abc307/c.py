import sys
from itertools import product


def input():
    return sys.stdin.readline().rstrip()


def same(G, S, HX, WX):
    for x in range(HX):
        for y in range(WX):
            if G[x][y] != S[x][y]:
                return False
    return True


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    def input_parse():
        H, W = mi()
        S = [input() for _ in range(H)]
        return H, W, S

    HA, WA, SA = input_parse()
    HB, WB, SB = input_parse()
    HX, WX, SX = input_parse()

    posA = list(product(range(-HA + 1, HX), range(-WA + 1, WX)))
    posB = list(product(range(-HB + 1, HX), range(-WB + 1, WX)))

    AXY = list(product(range(HA), range(WA)))
    BXY = list(product(range(HB), range(WB)))

    for (dha, dwa), (dhb, dwb) in product(posA, posB):
        G = [["."] * WX for _ in range(HX)]
        flag = True

        for x, y in AXY:
            if SA[x][y] == ".":
                continue
            xa = x + dha
            ya = y + dwa
            if not (0 <= xa < HX and 0 <= ya < WX):
                # 含まれるべき "#" が範囲外にある
                flag = False
            if flag:
                G[xa][ya] = "#"

        for x, y in BXY:
            if SB[x][y] == ".":
                continue
            xb = x + dhb
            yb = y + dwb
            if not (0 <= xb < HX and 0 <= yb < WX):
                # 含まれるべき "#" が範囲外にある
                flag = False
            if flag:
                G[xb][yb] = "#"

        if flag:
            if same(G, SX, HX, WX):
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
