def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    B = sorted(A.copy())
    for i in range(N):
        if B[-1] == A[i]:
            print(B[-2])
        else:
            print(B[-1])


if __name__ == "__main__":
    main()
