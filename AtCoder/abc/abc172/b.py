S = input()
T = input()
t = sum(i == j for i, j in zip(S, T))
print(len(S) - t)
