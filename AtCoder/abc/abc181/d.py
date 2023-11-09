from collections import Counter


def main():
    s = list(input())
    s = list(map(int, s))
    N = len(s)
    s = Counter(s)
    if N >= 2:
        st = 104 if N > 2 else 16
        en = 1000 if N > 2 else 100
        for j in range(st, en, 8):
            k = list(map(int, list(str(j))))
            k = Counter(k)
            if 0 in k:
                continue
            if all(key in s and s[key] >= k[key] for key in k.keys()):
                print("Yes")
                exit()
        print("No")
    else:
        if 8 in s:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
