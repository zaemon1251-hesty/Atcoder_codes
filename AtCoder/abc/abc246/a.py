from itertools import permutations


def main():
    A = [list(map(int, input().split())) for _ in range(3)]
    for x, y, z in permutations(range(3)):
        if A[x][0] == A[y][0]:
            if A[z][1] == A[x][1]:
                print(A[z][0], A[y][1])
            else:
                print(A[z][0], A[x][1])
            exit()


if __name__ == '__main__':
    main()
