A, B, C, D, E, F, X = map(int, input().split())
tk_t = A * (X // (A + C)) + min(A, X % (A + C))
ao_t = D * (X // (D + F)) + min(D, X % (D + F))
if tk_t * B > ao_t * E:
    print("Takahashi")
elif tk_t * B < ao_t * E:
    print("Aoki")
else:
    print("Draw")
