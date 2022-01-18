from bisect import bisect_right
N, D, A = map(int, input().split())
H = []
ans = 0
x_box = []
for i in range(N):
    x, h = map(int, input().split())
    H.append((x, h))
    x_box.append(x)
H.sort(key=lambda x: x[0])
x_box.sort()
buf = [0] * (N + 4)
D *= 2
for l in range(N):
    if l > 0:
        buf[l] += buf[l-1]
    if buf[l] < H[l][1]:
        r = l + 1
        r = bisect_right(x_box, D+H[l][0])
        d = H[l][1] - buf[l]
        cnt = (d + A - 1) // A
        buf[l] += A * cnt
        buf[r] -= A * cnt
        ans += cnt
print(ans)
_name__ == '__main__':
# maina()
# mainb()
# mainc()
# maind()
# maine()
mainf()
