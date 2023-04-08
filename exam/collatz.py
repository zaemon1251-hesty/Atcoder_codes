import sys


sys.setrecursionlimit(10**6)


def collatz_conjecture(n: int, count: int = 0) -> int:
    """
    正の整数nを入力として受け取り、nが1になるまで次の操作を繰り返す回数を返す。
    - nが偶数の場合、nを2で割る
    - nが奇数の場合、nを3倍して1を足す

    Parameters
    ----------
    n : int
        操作の対象となる正の整数

    Returns
    -------
    int
        nが1になるまでの操作回数
    """
    if n == 1:
        return count
    if n % 2 == 0:
        return collatz_conjecture(n // 2, count + 1)
    else:
        return collatz_conjecture(n * 3 + 1, count + 1)


if __name__ == "__main__":
    ans = collatz_conjecture(1243)
    print(ans)
