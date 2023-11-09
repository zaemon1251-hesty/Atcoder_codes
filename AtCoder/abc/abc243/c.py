from collections import defaultdict


def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    S = list(input())
    axis = defaultdict(list)
    for i, t in enumerate(A):
        a, b = t
        axis[b].append((a, i))
    for k, vs in axis.items():
        if len(vs) < 2:
            continue
        vs.sort(key=lambda x: x[0])
        r = False
        for a, i in vs:
            if S[i] == "R":
                r = True
            if S[i] == "L" and r:
                print("Yes")
                exit()
    print("No")


if __name__ == "__main__":
    main()
