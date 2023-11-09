#! /usr/env/python

import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = list(input())
    newS = []
    for s in S:
        if s == "A":
            newS.extend(list("BB"))
        else:
            newS.append(s)
    res = []
    for i, s in enumerate(newS):
        if res and s == "B" and res[-1] == "B":
            res.pop()
            s = "A"
        res.append(s)
    print("".join(res))


if __name__ == "__main__":
    main()
