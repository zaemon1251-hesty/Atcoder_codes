def main():
    n, m = map(int, input().split())
    x = []
    for i in range(m):
        n1, k1 = map(int, input().split())
        x.append((n1, k1))
    x = sorted(x, key=lambda x: (x[0], x[1]))
    ans = set()
    ans.add(n)
    now = x[0][0]
    black = set()
    for i in range(m):
        xi, yi = x[i]
        if now == xi:
            black.add(yi)
            continue
        else:
            a = set()
            b = set()
            for Y in black:
                if ((Y - 1 in ans) or (Y + 1 in ans)) and (Y not in ans):
                    a.add(Y)
                elif ((Y - 1 not in ans) and (Y + 1 not in ans)) and (Y in ans):
                    b.add(Y)
            for j in a:
                ans.add(j)
            for j in b:
                ans.discard(j)
            now = xi
            black = set([yi])
    a = set()
    b = set()
    for Y in black:
        if ((Y - 1 in ans) or (Y + 1 in ans)) and (Y not in ans):
            a.add(Y)
        elif ((Y - 1 not in ans) and (Y + 1 not in ans)) and (Y in ans):
            b.add(Y)
    for j in a:
        ans.add(j)
    for j in b:
        ans.discard(j)
    print(len(ans))


if __name__ == '__main__':
    main()
