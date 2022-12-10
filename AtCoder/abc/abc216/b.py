from itertools import combinations


def main():
    N = int(input())
    Users = [input().split() for __ in range(N)]
    for i, j in combinations(range(N), 2):
        if all(Users[i][name] == Users[j][name] for name in range(2)):
            print("Yes")
            exit(0)
    print("No")


if __name__ == '__main__':
    main()
