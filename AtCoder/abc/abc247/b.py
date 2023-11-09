from collections import defaultdict


def main():
    N = int(input())
    A = [list(map(str, input().split())) for _ in range(N)]
    say = defaultdict(int)
    may = defaultdict(int)
    names = defaultdict(int)
    for s, t in A:
        if s in say and t in may:
            print("No")
            exit()
        say[s] += 1
        may[t] += 1
        names[s] += 1
        names[t] += 1
    for s, t in A:
        if s != t and names[s] > 1 and names[t] > 1:
            print("No")
            exit()
        elif s == t and names[s] > 2:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
