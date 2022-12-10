n = int(input())
a = list(range(1, n + 1))
print(sum(i for i in a if i % 3 != 0 and i % 5 != 0))
