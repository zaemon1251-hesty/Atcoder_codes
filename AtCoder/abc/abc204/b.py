N = int(input())
A = list(map(int, input().split()))
print(sum(max(i - 10, 0) for i in A))
