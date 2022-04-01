N = int(input())
S = set(range(2002))
A = set(map(int, input().split()))
print(min(S - A))
