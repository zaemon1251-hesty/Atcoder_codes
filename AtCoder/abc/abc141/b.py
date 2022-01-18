S = list(input())
odd = {"R", "U", "D"}
even = {"L", "U", "D"}
print("Yes" if set(S[::2]) <= odd and set(S[1::2]) <= even else "No")
