X = int(input())
for a in range(-250, 250):
    for b in range(-250, 250):
        if a**5 - b**5 == X:
            print(a, b)
            exit()
