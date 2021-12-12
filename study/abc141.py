def maina():
    S = input()
    if S[0] == "C":
        ans = "Rainy"
    elif S[0] == "S":
        ans = "Cloudy"
    else:
        ans = "Sunny"
    print(ans)


def mainb():
    S = list(input())
    odd = {"R", "U", "D"}
    even = {"L", "U", "D"}
    print("Yes" if set(S[::2]) <= odd and set(S[1::2]) <= even else "No")


def mainc():
    N, K, Q = map(int, input().split())
    A = [0] * N
    for _ in range(Q):
        t = int(input()) - 1
        A[t] += 1
    for a in A:
        print("Yes" if Q - a < K else "No")


mainc()
