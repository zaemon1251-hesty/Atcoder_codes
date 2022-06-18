def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = [0] * 4
    ans = 0
    for a in A:
        P[0] = 1
        tmp = [0] * 4
        for i in range(4):
            if P[i]:
                if i + a >= 4:
                    ans += 1
                else:
                    tmp[i + a] = 1
        P = tmp
    print(ans)


if __name__ == '__main__':
    main()
