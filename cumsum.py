
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

def interval(A, K):
    #尺取り法
    #和がKとなる区間のうち最大の長さを求める
    ans = 0
    N = len(A)
    _sum = 0
    right = 0
    for left in range(N):
        while right < N and _sum + A[right] <= K:
            _sum += A[right]
            right += 1
            ans = max(ans, right - left + 1)
        if left == right:right += 1
        _sum -= A[left]
    return ans



if __name__ == "__main__":
    tmp, f = two_cumsum([[1,2,3,4,5], [2,4,6,8,10]])

    print(f"[0,2)×[0,3) 区間の和 = {f[2][3]} - {f[0][0]}")