X = int(input())
a = 100
t = 0
while X > a:
    a *= 1.01
    a = int(a)
    t += 1
print(t)
