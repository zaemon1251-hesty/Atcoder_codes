def main():
    N = int(input())
    A = list(map(int, input().split()))
    cand = list(range(len(A)))
    while len(cand) > 2:
        r = []
        T = len(cand)
        for i in range(1, T, 2):
            t1, t2 = cand[i - 1], cand[i]
            if A[t1] > A[t2]:
                r.append(t1)
            else:
                r.append(t2)
        cand = r
    t1, t2 = cand[0], cand[1]
    if A[t1] < A[t2]:
        print(t1 + 1)
    else:
        print(t2 + 1)


if __name__ == "__main__":
    main()
