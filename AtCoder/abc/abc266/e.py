def main():
    N = int(input())

    def Edp(i: int) -> float:
        if i == N:
            return 3.5
        thres = Edp(i + 1)
        sup = int(thres) + 1
        res = 0
        res += sum(range(sup, 6 + 1)) / 6
        res += thres * (sup - 1) / 6
        return res

    print(Edp(1))


if __name__ == '__main__':
    main()
