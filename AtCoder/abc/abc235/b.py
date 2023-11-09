N = int(input())
H = list(map(int, input().split()))
i = 0
while i < N - 1 and H[i] < H[i + 1]:
    i += 1
print(H[i])
