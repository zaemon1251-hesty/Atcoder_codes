from itertools import combinations


def main():
    allowlist = [("W", "L"), ("L", "W"), ("D", "D")]
    N = int(input())
    A = [list(input()) for _ in range(N)]
    for i, j in combinations(range(N), 2):
        if (A[i][j], A[j][i]) not in allowlist:
            print("incorrect")
            exit()
    print("correct")


if __name__ == "__main__":
    main()
