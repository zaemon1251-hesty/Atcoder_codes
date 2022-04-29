def main():
    inf = 1 << 60
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    ans = -inf
    for x in [a, b]:
        for y in [c, d]:
            ans = max(ans, x - y)
    print(ans)


if __name__ == '__main__':
    main()
