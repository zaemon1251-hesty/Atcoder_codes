
def one_cumsum(arr):
    """
    [l, r)の区間和が
    f(r) - f(l)　で求められるデータ構造 (0-index)
    """
    from itertools import accumulate

    return [0] + list(accumulate(arr))


def two_cumsum(arr):
    """
    [x1,x2) × [y1,y2) の区間和が
    f(x2,y2) - f(x1,y2) - f(x2,y1) + f(x1,y1)　で求められるデータ構造 (0-index)
    """
    import copy

    tmp = [[0] * (len(arr[0]) + 1)]
    for i in range(len(arr)):
        tmp.append(one_cumsum(arr[i]))

    s = copy.deepcopy(tmp)

    for i in range(len(arr)):
        for j in range(len(arr[0]) + 1):
            s[i+1][j] += s[i][j]

    return tmp, s





if __name__ == "__main__":
    tmp, f = two_cumsum([[1,2,3,4,5], [2,4,6,8,10]])

    print(f"[0,2)×[0,3) 区間の和 = {f[2][3]} - {f[0][0]}")