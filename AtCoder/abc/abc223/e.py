def divceil(x, y):
    return (x + y - 1) // y
x, y, a, b, c = map(int, input().split())
edge = (x, y)
rectangle = (a, b, c)
import itertools
for i, j in itertools.permutations(edge, r=None):
    if sum(divceil(k, i) for k in rectangle) <= j:
        print("Yes")
        return
for d, e, f in itertools.permutations(rectangle, r=None):
    for i, j in itertools.permutations(edge, r=None):
        g = j - divceil(d, i)
        if g <= 0:
            continue
        if divceil(e, g) + divceil(f, g) <= i:
            print("Yes")
            return
print("No")
