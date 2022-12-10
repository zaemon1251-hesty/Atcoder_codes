a, b, c, d = map(int, input().split())
i = True
tak = (c + b - 1) // b
aok = (a + d - 1) // d
print("Yes" if tak <= aok else "No")
