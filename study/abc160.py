x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse = True)
q.sort(reverse = True)
r.sort(reverse = True)

apples = sorted(p[:x] + q[:y] + r, reverse = True)
print(sum(apples[: x + y]))