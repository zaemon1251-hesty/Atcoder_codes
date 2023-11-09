def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    pa, pb = True, True
    for i in range(1, N):
        tpa, tpb = True, True
        if (pa and abs(A[i] - A[i - 1]) <= K) or (pb and abs(A[i] - B[i - 1]) <= K):
            pass
        else:
            tpa = False
        if (pa and abs(B[i] - A[i - 1]) <= K) or (pb and abs(B[i] - B[i - 1]) <= K):
            pass
        else:
            tpb = False
        pa, pb = tpa, tpb
    print("Yes" if (pa or pb) else "No")


if __name__ == "__main__":
    main()
