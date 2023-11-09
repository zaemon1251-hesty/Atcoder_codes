k = int(input())
p = list("0123456789")

todo = [*p[1:]]
for j in range(k - 1):
    i = todo[j]
    lat = p.index(i[-1])
    if lat != 0:
        todo.append(i + p[lat - 1])
    todo.append(i + p[lat])
    if lat != 9:
        todo.append(i + p[lat + 1])
print(todo[k - 1])
