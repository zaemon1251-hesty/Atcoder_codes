S = list(input())
T = list(input())
mod = 26
for i in range(mod):
    S = [chr((ord(S[t]) - ord("a") + mod - 1) % mod + ord("a"))
         for t in range(len(S))]
    if S == T:
        print("Yes")
        return
print("No")
