from collections import defaultdict


def main():
    N = int(input())
    SS = [input() for _ in range(N)]
    cnts = defaultdict(int)
    for s in SS:
        u = cnts[s]
        if u == 0:
            print(s)
        else:
            print(s + f"({u})")
        cnts[s] += 1


if __name__ == '__main__':
    main()
