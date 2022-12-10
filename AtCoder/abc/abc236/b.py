N = int(input())
A = list(map(int, input().split()))
s = [0] * N
for i in range(len(A)):
    s[A[i] - 1] += 1
for i in range(N):
    if s[i] == 3:
        print(i + 1)
        exit()
