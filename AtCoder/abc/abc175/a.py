S = list(input())
if S.count("R") == 2:
    if S[1] != "R":
        S[0] = "T"
print(S.count("R"))
