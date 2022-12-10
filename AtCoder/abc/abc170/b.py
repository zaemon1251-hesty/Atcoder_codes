X, Y = map(int, input().split())
for x in range(X+1):
    for y in range(X + 1):
        if x + y == X and 2 * x + 4*y == Y:
            print("Yes")
            exit()
print("No")
