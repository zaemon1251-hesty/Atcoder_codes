def main():
    T = int(input())
    S = list(int(input()) for _ in range(T))
    for N in S:
        ans_set = []
        num = str(N)
        length = len(num)
        for l in range(1, length // 2 + 1):
            if length % l != 0:
                continue
            flg = True
            ws = []
            for i in range(0, length, l):
                s = int(num[i:i + l])
                ws.append(int(num[i:i + l] * l))
            ans_set.append(min(ws))
        print(max(ans_set))


if __name__ == '__main__':
    main()
