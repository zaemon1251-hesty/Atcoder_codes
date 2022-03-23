def main():
    X = int(input())
    M = int(input())
    nums = list(map(int, list(str(X))))

    def check(m):
        res = 0
        prod = 1
        for i in range(len(nums)):
            res += nums[-1 - i] * prod
            prod *= m
        return res <= M

    ok = max(nums)
    ng = 10**18 + 1

    if ok == 0 or (len(nums) == 1 and nums[0] <= M):
        print(1)
        exit()

    if (len(nums) == 1 and nums[0] > M):
        print(0)
        exit()

    while ng - ok > 1:
        cen = (ng + ok) // 2
        if check(cen):
            ok = cen
        else:
            ng = cen
        assert ng != ok
    print(ok - max(nums))


if __name__ == '__main__':
    main()
