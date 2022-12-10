def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = [a + b for a, b in zip(A, B)]
    A = sorted(enumerate(A), key=lambda x: x[1], reverse=True)
    B = sorted(enumerate(B), key=lambda x: x[1], reverse=True)
    AB = sorted(enumerate(AB), key=lambda x: x[1], reverse=True)
    print(A, B, AB)
    passes = set()
    cnt = 0
    i = 0
    while cnt < X:
        if A[i][0] + 1 not in passes:
            passes.add(A[i][0] + 1)
            cnt += 1
        i += 1

    i = 0
    while cnt < X + Y:
        if B[i][0] + 1 not in passes:
            passes.add(B[i][0] + 1)
            cnt += 1
        i += 1

    i = 0
    while cnt < X + Y + Z:
        if AB[i][0] + 1 not in passes:
            passes.add(AB[i][0] + 1)
            cnt += 1
        i += 1

    print(*sorted(passes), sep="\n")


if __name__ == '__main__':
    main()
