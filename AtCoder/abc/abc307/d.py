import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    S = list(input())
    que = deque([])
    dels = []
    for i, s in enumerate(S):
        if s == "(":
            que.append(i)
        elif s == ")":
            if que:
                st = que.pop()
                en = i + 1
                dels.append((st, en))

    if dels:
        dels.sort(key=lambda x: x[0])
        new_dels = [dels[0]]
        for i, (st, en) in enumerate(dels):
            prev_st, prev_en = new_dels[-1]
            if prev_en <= st:
                new_dels.append((st, en))
        dels = new_dels

    ans = ""
    cur_i = 0
    for del_i, (st, en) in enumerate(dels):
        ans += "".join(S[cur_i:st])
        cur_i = en

    if cur_i != N:
        ans += "".join(S[cur_i:])
    print(ans)


if __name__ == "__main__":
    main()
