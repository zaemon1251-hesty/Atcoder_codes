from bisect import bisect_left, bisect_right
from string import ascii_lowercase


def main():
    S = list(input())
    T = list(input())
    ti = 0
    ans = 0
    token_locs = {a: [] for a in ascii_lowercase}
    for i, s in enumerate(S):
        token_locs[s].append(i + 1)

    ans = 0
    loc = 0
    for ti in T:
        if len(token_locs[ti]) == 0:
            print(-1)
            exit()

        idx = bisect_right(token_locs[ti], loc)
        if idx >= len(token_locs[ti]):
            newLoc = token_locs[ti][0]
            ans += len(S) - loc + newLoc
        else:
            newLoc = token_locs[ti][idx]
            ans += newLoc - loc
        loc = newLoc

    print(ans)


if __name__ == "__main__":
    main()
