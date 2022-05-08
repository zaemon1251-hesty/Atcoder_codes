def main():
    N = int(input())
    A = [list(map(str, input().split()))for _ in range(N)]
    A.sort(key=lambda x: int(x[1]), reverse=True)
    print(A[1][0])


if __name__ == '__main__':
    main()
