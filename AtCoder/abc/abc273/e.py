import sys
input = sys.stdin.readline
Q = int(input())
A = [-1]
prev = [-1]
note = dict()
idx = 0
n = 0
for i in range(Q):
    x = list(input().split())
    if x[0] == "ADD":
        a = int(x[1])
        A.append(a)
        prev.append(idx)
        n += 1
        idx = n
    elif x[0] == "DELETE":
        if idx != 0:
            idx = prev[idx]
    elif x[0] == "SAVE":
        a = int(x[1])
        note[a] = idx
    elif x[0] == "LOAD":
        a = int(x[1])
        idx = note.get(a, 0)
    print(A[idx], end=" ")
