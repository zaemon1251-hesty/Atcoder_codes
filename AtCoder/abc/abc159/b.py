S = list(input())
N = len(S)
a = (N - 1) // 2
b = (N + 3) // 2 - 1
def iskaibun(arr):
    return all(i == j for i, j in zip(arr, arr[::-1]))
print("Yes" if all([iskaibun(S), iskaibun(
    S[:a]), iskaibun(S[b:])]) else "No")
