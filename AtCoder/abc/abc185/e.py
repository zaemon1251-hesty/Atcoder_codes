from functools import lru_cache
import sys
sys.setrecursionlimit(2*10**6)


def main():
    N, M = map(int, input().split())
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))

    @lru_cache(maxsize=None)
    def ld(s, t):
        # 編集距離
        '''文字列のレーベンシュタイン距離を計算する'''

        # 一方が空文字列(Array[key:] == [])なら、他方の長さが求める距離
        if s == N-1:
            return M - t
        if t == M-1:
            return N - s

        # 一文字目が一致なら、二文字目以降の距離が求める距離
        if A[s] == B[t]:
            return ld(s+1, t+1)

        # 一文字目が不一致なら、追加／削除／置換のそれぞれを実施し、
        # 残りの文字列についてのコストを計算する

        # Sの先頭に追加
        l1 = ld(s, t+1)

        # Sの先頭を削除
        l2 = ld(s+1, t)

        # Sの先頭を置換
        l3 = ld(s+1, t+1)

        # 追加／削除／置換を実施した分コスト（距離）1の消費は確定
        # 残りの文字列についてのコストの最小値を足せば距離となる
        return 1 + min(l1, l2, l3)

    print(ld(0, 0))

def main2():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    inf=pow(10,10)
    dp=[[inf]*(m+1) for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j]=i+j
            else:
                k=int(a[i-1]!=b[j-1])
                dp[i][j]=min(dp[i][j],dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+k)
    print(dp[n][m])


if __name__ == '__main__':
    main2()
