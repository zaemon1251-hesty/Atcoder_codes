N, K, Q = map(int, input().split())
A = [0] * N
for _ in range(Q):
    t = int(input()) - 1
    A[t] += 1
for a in A:
    print("Yes" if Q - a < K else "No")
c()
