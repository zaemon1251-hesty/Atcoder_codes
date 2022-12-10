from typing import List


def sub() -> None:
    N, K = map(int, input().split())
    A = list(map(lambda x: int(x) - 1, input().split()))
    seen = [False] * N
    path = []
    cr = 0
    while not seen[cr]:
        seen[cr] = True
        path.append(cr)
        cr = A[cr]

    chain = path.index(cr)
    cycle = len(path) - chain

    if K < chain:
        print(path[K] + 1)
    else:
        K -= chain
        K %= cycle
        print(path[chain + K] + 1)


def main():
    # ダブリング
    # 入力受け取り
    N, K = map(int, input().split())
    # 0-indexedで受け取っておく
    A: List[int] = list(map(lambda x: int(x) - 1, input().split()))

    # ダブリングのテーブル
    dp: List[List[int]] = [[0 for j in range(N)] for i in range(61)]
    # 初期条件
    for j in range(N):
        dp[0][j] = A[j]

    # 遷移
    for i in range(1, 61):
        for j in range(N):
            dp[i][j] = dp[i - 1][dp[i - 1][j]]

    # 解を求める
    answer: int = 0
    # 現在見ているビットの下位からの桁
    i: int = 0
    # Kを2進数とみなして計算する
    while K:
        # Kの下位からi桁目が1なら遷移する
        if K & 1:
            answer = dp[i][answer]
        # 1つビットシフトする
        K >>= 1
        # iを進める
        i += 1

    # 解の出力(1-indexedに戻す)
    print(answer + 1)


if __name__ == "__main__":
    main()
