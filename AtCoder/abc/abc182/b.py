def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = -1
    _max = 0
    for i in range(2, 1001):
        tmp = 0
        for a in A:
            if a % i == 0:
                tmp += 1
        if tmp >= _max:
            _max = tmp
            ans = i

    print(ans)


if __name__ == "__main__":
    main()
