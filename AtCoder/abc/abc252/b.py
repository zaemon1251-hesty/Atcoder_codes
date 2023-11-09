from collections import Counter


def main():
    H, W = map(int, input().split())
    A = list(map(int, input().split()))
    B = set(map(int, input().split()))
    ans = False

    for i, a in enumerate(A):
        if i + 1 in B and a == max(A):
            ans = True
    print("Yes" if ans else "No")


if __name__ == "__main__":
    main()
