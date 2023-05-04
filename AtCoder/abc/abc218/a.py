<<<<<<< HEAD
def main():
    N = int(input())
    S = list(input())
    print("Yes" if S[N - 1] == "o" else "No")


if __name__ == '__main__':
    main()
=======
N = int(input())
S = set()
T = set()
def zerolize(P):
    mx, my = min(P)
    tmp = set()
    for x, y in P:
        tmp.add((x-mx, y-my))
    return tmp
def rot(P):
    tmp = set()
    for x, y in P:
        tmp.add((y, -x))
    return tmp
for i in range(N):
    A = list(input())
    for j in range(N):
        if A[j] == "#":
            S.add((i, j))
for i in range(N):
    A = list(input())
    for j in range(N):
        if A[j] == "#":
            T.add((i, j))
for _ in range(4):
    S = zerolize(S)
    T = zerolize(T)
    if S == T:
        print("Yes")
        exit()
    S = rot(S)
else:
    print("No")
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
