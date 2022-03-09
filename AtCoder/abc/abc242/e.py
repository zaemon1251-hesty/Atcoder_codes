from copy import copy


def main():
    MOD = 998244353
    T = int(input())
    cases = [[int(input()), input().lower()] for _ in range(T)]
    ans = []
    a = ord("a")
    for t in cases:
        tmp = 0
        n, s = t
        # 争点となる長さ
        k = (n + 1) // 2
        # AA...A(KコのAが並んでいる状態)
        tmp += 1
        # 長さが固定なら26進数として扱える
        odd = 1 if n % 2 != 0 else 0
        for i in range(k):
            tmp += (ord(s[i]) - a) * pow(26, k - 1 - i, MOD)
            tmp %= MOD
        try:
            for i in range(n // 2):
                if s[n // 2 - 1 - i] > s[k + i]:
                    tmp -= 1
                    break
                elif s[n // 2 - 1 - i] < s[k + i]:
                    break
        except IndexError as e:
            print(i, n // 2 - 1 - i, k + i)
            print(e)
        ans.append(tmp % MOD)
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
