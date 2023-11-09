N, x = map(int, input().split())
a = list(map(int, input().split()))
print("Yes" if sum(a) - N // 2 <= x else "No")
