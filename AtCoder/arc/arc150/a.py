import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    T = ii()
    for _ in range(T):
        N, K = mi()
        S = input()

        cnt_1_l = 0
        cnt_1_m = S[:K].count("1")
        cnt_0_m = S[:K].count("0")
        cnt_1_r = S.count("1") - cnt_1_m - cnt_1_l

        ans = bool(cnt_0_m == cnt_1_l == cnt_1_r == 0)

        for en in range(K, N):
            rm_i = en - K

            if S[rm_i] == "1":
                cnt_1_l += 1
                cnt_1_m -= 1
            elif S[rm_i] == "0":
                cnt_0_m -= 1

            if S[en] == "1":
                cnt_1_r -= 1
                cnt_1_m += 1
            elif S[en] == "0":
                cnt_0_m += 1

            res = bool(cnt_0_m == cnt_1_l == cnt_1_r == 0)
            if res and ans:
                ans = False
                break
            ans |= res

        print("Yes" if ans else "No")


if __name__ == '__main__':
    main()
