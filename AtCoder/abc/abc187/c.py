def main():
    N = int(input())
    S = list(input() for _ in range(N))
    t = set()
    for s in S:
        if s[0] != "!" and "!"+s in t or s[0] == "!" and s[1:] in t:
            s = s.replace("!", "")
            print(s)
            exit()
        t.add(s)
    else:
        print("satisfiable")


if __name__ == '__main__':
    main()