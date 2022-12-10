X = input()
if len(X) == 1:
    print(0)
elif len(X) == 2 and X[0] == "-":
    print(-1)
else:
    if X[0] == "-":
        t = X[-1]
        X = int(X[:-1])
        X -= int(t != "0")
        print(X)
    else:
        X = int(X[:-1])
        print(X)
