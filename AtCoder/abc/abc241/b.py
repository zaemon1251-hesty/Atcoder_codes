from collections import Counter


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = Counter(A)
    for b in B:
        t = A.get(b, 0)
        if t == 0:
            print("No")
            exit()
        else:
            A[b] -= 1
    print("Yes")


if __name__ == "__main__":
    main()
