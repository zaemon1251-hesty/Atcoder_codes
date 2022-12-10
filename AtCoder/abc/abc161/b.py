N, M = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
print("Yes" if sum(i * 4 * M >= s for i in a) >= M else "No")
