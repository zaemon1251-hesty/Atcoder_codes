from collections import Counter


def main():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    S = input()
    c = Counter(S)
    if len(c.keys()) == 2 and all(v == 2 for v in c.values()):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
