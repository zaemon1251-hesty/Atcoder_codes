import sys


def input():
    return sys.stdin.readline().rstrip()


def mov(A, m, i):
    B = A.copy()
    for k in range(i):
        for j in range(m):
            B[j] = A[B[j] - 1]
    return B


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    cycles = [2 ** 2, 3 ** 2, 5, 7, 11, 13, 17, 19, 23]

    def gen_seq():
        seq = []
        for c in cycles:
            seq.extend([(i + 1) % c + len(seq) + 1 for i in range(c)])
        return seq

    seq = gen_seq()
    print(len(seq))
    print(*seq)

    seq2 = list(map(int, input().split()))
    # seq2 = mov(seq, len(seq), 2)
    assert len(seq2) == len(seq)
    # print(*seq2)

    rems = []
    offset = 0
    for size in cycles:
        rems.append(seq2[offset] - (offset + 1))
        offset += size

    x, mm = 0, 1
    for r, m in zip(rems, cycles):
        while x % m != r:
            x += mm
        mm *= m

    print(x)


if __name__ == '__main__':
    main()
