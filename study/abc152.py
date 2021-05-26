def get_nums(n):
    return int(str(n)[0]), int(str(n)[-1])


def count_strict_vals(n, a, b):
    """
    ABC152D
    Nが二桁以上のときかつ（一桁のNが入力されたら0で返す）
    A(最上位桁の数字a, 最下位桁の数字b)の桁数がNの桁数と同じであるとき、
    制約を満たすAの総数を求める。
    """
    n =str(n)
    a = str(a)
    b = str(b)
    if a > n[0] or len(n) == 1:
        return 0
    elif a < n[0]:
        return pow(10, len(n) - 2)
    else:
        ans = 0
        for i, v in zip(range(1, len(n) - 1), n[1:-1]):
            if i == len(n) - 2 and b <= n[-1]:
                ans += 1
            ans += int(v) * pow(10, len(n) - 2 - i)
        else:
            ans += int(int(n[:-1]+b) <= int(n))

        return ans



def maina():
    n, m = map(int, input().split())
    print("Yes" if n == m else "No")


def mainb():
    a, b = map(int, input().split())
    a, b = str(a) * b, str(b) * a
    print(min(a, b))


def mainc():
    n = int(input())
    p = list(map(int, input().split()))
    min_ = float("inf")
    ans = 0
    for i in range(n):
        if p[i] <= min_:
            ans += 1
            min_ = p[i]
    print(ans)


def maind():
    from itertools import permutations
    N = int(input())

    cnt = [[0]*10 for _ in range(10)]

    for b in range(1, N + 1):
        x, y = get_nums(b)
        cnt[x][y] += 1

    ans = 0
    for i in range(1,10):
        for j in range(1,10):
            ans += cnt[i][j]*cnt[j][i]
    print(ans)



def maine():
    h, n = map(int, input().split())
    A, B = [], []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)



if __name__ == '__main__':
    #maina()
    #mainb()
    #mainc()
    maind()
    #maine()