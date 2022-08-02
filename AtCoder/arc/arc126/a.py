def main():
    T = int(input())
    for _ in range(T):
        n1, n3, n2 = map(int, input().split())
        n3 //= 2

        n32 = min(n3, n2)
        n3 -= n32
        n2 -= n32

        n113 = min(n3, n1 // 2)
        n1 -= n113 * 2
        n3 -= n113

        n221 = min(n2 // 2, n1)
        n2 -= n221 * 2
        n1 -= n221

        n2111 = min(n2, n1 // 3)
        n2 -= n2111
        n1 -= n2111 * 3

        n11111 = n1 // 5
        n1 -= n11111 * 5

        print(n32 + n113 + n221 + n2111 + n11111)


if __name__ == '__main__':
    main()
