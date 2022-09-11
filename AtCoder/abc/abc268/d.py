from bisect import bisect, bisect_left
from itertools import combinations_with_replacement, permutations


def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = sorted([input() for _ in range(M)])
    le = sum(len(s) for s in S) + N - 1
    bar = 16 - le
    perms = permutations(range(N), N)
    cmbs = combinations_with_replacement(range(bar + 1), N - 1)

    for perm in perms:
        for cmb in cmbs:
            # cmb
            cmb = list(cmb)
            cmb.append(16)

            # gen string
            res = ""
            bar_prev = 0
            for i, (s_i, bar_num) in enumerate(zip(perm, cmb)):
                res += S[s_i]
                if i != N - 1:
                    res += "_" * (1 + bar_num - bar_prev)
                    bar_prev = bar_num

            # answer
            if 3 <= len(res) <= 16:
                j = bisect_left(T, res)
                if j >= M or T[j] != res:
                    print(res)
                    exit()
    print(-1)


def sub():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N, M = mi()

    S = [input() for i in range(N)]
    T = set([input() for i in range(M)])

    def dfs(X, S, margin):  # Xは現在の文字列、Sは未探索の文字列のリスト
        # print('X',X)
        # print('S',S)
        # print('margin',margin)
        if len(S) == 0:  # 探索終了
            if len(X) >= 3 and X not in T:  # 条件(3文字以上、Tに無い)にあてはまるか
                print(X)
                exit()
            return
        for i in range(len(S)):  # 残りのうち1つを選ぶ
            SS = S[:i] + S[i + 1:]
            for c in range(1, margin + 1):
                dfs(X + "_" * c + S[i], SS, margin - c)

    margin = 16 - sum(map(len, S))
    for i in range(len(S)):
        dfs(S[i], S[:i] + S[i + 1:], margin)
    print(-1)


if __name__ == '__main__':
    sub()
