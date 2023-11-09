from math import inf


def main():
    N = int(input())
    H = list(map(int, input().split()))
    cur = inf
    for i in range(N - 1, -1, -1):
        if cur - H[i] < 0:
            break
        elif cur - H[i] == 0:
            cur = H[i]
        else:
            cur = H[i] + 1
    else:
        print("Yes")
        exit()
    print("No")


if __name__ == "__main__":
    main()
