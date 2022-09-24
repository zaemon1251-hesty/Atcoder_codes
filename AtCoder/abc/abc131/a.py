import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N = input()
    for i in range(len(N) - 1):
        if N[i] == N[i + 1]:
            print("Bad")
            exit()
    print("Good")


if __name__ == '__main__':
    main()
