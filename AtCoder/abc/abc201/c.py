def main():
    S = list(input())
    ans = 0
    cnum = S.count("o")
    for i in range(10000):
        d = "%04d" % i
        flg = True
        cn = 0
        for j, e in enumerate(S):
            if e == "o":
                if str(j) not in d:
                    flg = False
                else:
                    cn += 1
            elif e == "x" and str(j) in d:
                flg = False
        if cn != cnum:
            flg = False
        ans += int(flg)

    print(ans)


if __name__ == '__main__':
    main()
