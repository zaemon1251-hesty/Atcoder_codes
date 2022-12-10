def main():
    L, R = map(int, input().split())
    if L % 2019 == 0 or L // 2019 < R // 2019:
        print(0)
    else:
        buf = [0] * 2019
        for i in range(L, R + 1):
            buf[i % 2019] += 1

        ans = 2019
        for k in range(2019):
            if buf[k] == 0:
                continue
            if buf[k] > 1:
                ans = min(ans, (k * k) % 2019)
            for m in range(k + 1, 2019):
                if buf[m] > 0:
                    ans = min(ans, (k * m) % 2019)
        print(ans)


if __name__ == '__main__':
    main()
