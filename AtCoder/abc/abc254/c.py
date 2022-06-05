from math import gcd


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(A)
    if A == B:
        print("Yes")
        exit()
    E = [[] for i in range(K)]
    for i in range(N):
        E[i % K].append(A[i])
    for i in range(K):
        E[i] = sorted(E[i], reverse=True)

    ans = []
    i = 0
    while len(ans) < N:
        if E[i % K]:
            ans.append(E[i % K].pop())
        i += 1
    if ans == B:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
