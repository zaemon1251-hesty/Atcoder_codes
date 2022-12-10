N, K = map(int, input().split())
h = list(map(int, input().split()))
print(sum(i >= K for i in h))
