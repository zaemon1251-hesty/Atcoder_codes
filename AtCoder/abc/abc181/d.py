from collections import Counter


def main():
    s = list(input())
    N = len(s)
    s = list(map(int, s))
    s = Counter(s)
    if N >= 4:
        for j in range(8, 1000, 8):
            k = list(map(int, list(str(j))))
            k = Counter(k)
            if all(key in s and s[key] >= k[key] for key in k.keys()):
                print("Yes")
                exit()
        print("No")
    else:
        for j in range(8, 1000, 8):
            k = list(map(int, list(str(j))))
            k = Counter(k)


if __name__ == '__main__':
    main()
