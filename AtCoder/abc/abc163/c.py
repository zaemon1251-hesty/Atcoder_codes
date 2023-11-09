N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
b = [0 for _ in range(N)]
for i in range(N - 1):
    b[A[i]] += 1
print(*b, sep="\n")
