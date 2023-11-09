def main():
    s = input()
    for z in range(10):
        flg = True
        ss = "0" * z + s
        n = len(ss)
        for i in range(n // 2):
            if ss[i] != ss[-i - 1]:
                flg = False
                break
        if flg:
            print("Yes")
            exit()
    else:
        print("No")


if __name__ == "__main__":
    main()
