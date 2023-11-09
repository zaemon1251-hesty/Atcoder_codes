def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a, b = set(), set()

    newA, cntA = [], []
    for v in A:
        if v not in a:
            newA.append(v)
            a.add(v)
        cntA.append(len(newA))
    A = newA

    newB, cntB = [], []
    for v in B:
        if v not in b:
            newB.append(v)
            b.add(v)
        cntB.append(len(newB))
    B = newB

    Q = int(input())
    S = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]

    commons = set()
    mp = {}
    for i in range(min(len(A), len(B))):
        if A[i] in commons:
            commons.discard(A[i])
        else:
            commons.add(A[i])

        if B[i] in commons:
            commons.discard(B[i])
        else:
            commons.add(B[i])
        mp[i + 1] = len(commons) == 0

    print(*map(lambda x: "Yes" if (cntA[x[0]] == cntB[x[1]] and mp[cntA[x[0]]]) else "No", S), sep="\n")


if __name__ == "__main__":
    main()
