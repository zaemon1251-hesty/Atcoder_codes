import sys


def input():
    return sys.stdin.readline().rstrip()


ExceptionalEdges = {
    3: {"odd": [1, 3, 7], "even": [8, 6, 2]},
    4: {"odd": [1, 3, 5, 7], "even": [8, 6, 4, 2]},
    5: {"odd": [21, 1, 3, 9, 15], "even": [24, 8, 6, 12, 18]},
}


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    A = [-1] * (N**2)
    deck = set([i for i in range(1, N**2 + 1)])

    even_i = (N**2 + 1) // 2
    odd_i = even_i - 1

    # fill edge numbers
    if N <= 5:
        for od, ev in zip(ExceptionalEdges[N]["odd"][::-1], ExceptionalEdges[N]["even"]):
            deck.remove(od)
            deck.remove(ev)

            A[odd_i] = od
            A[even_i] = ev

            odd_i -= 1
            even_i += 1
    else:
        d = 3
        cnt = 0
        while cnt < 2 * N:
            deck.remove(d)

            if d % 2 == 1:
                A[odd_i] = d
                odd_i -= 1
            else:
                A[even_i] = d
                even_i += 1
            cnt += 1
            d += 3

    # fill the rest numbers
    for d in deck:
        if d % 2 == 1:
            A[odd_i] = d
            odd_i -= 1
        else:
            A[even_i] = d
            even_i += 1

    # OUTPUT
    for st in range(0, N**2, N):
        print(*A[st : st + N])


if __name__ == "__main__":
    main()
