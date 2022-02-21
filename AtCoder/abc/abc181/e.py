#  けんちょんさん参考
import bisect
inf = pow(10, 18)
n, m = map(int, input().split())
H = sorted(list(map(int, input().split())))
W = sorted(list(map(int, input().split())))

if n < 2:
    ans = inf
    for i in range(m):
        ans = min(ans, abs(H[0]-W[i]))
    print(ans)
    exit()

rest_m = [H[0]]
rest_x = [abs(H[0]-H[1])]
for i in range(1, n, 2):
    rest_m.append(rest_m[-1]+abs(H[i]-H[i+1]))

for i in range(2, n-1, 2):
    rest_x.append(rest_x[-1]+abs(H[i]-H[i+1]))
rest_x.append(rest_x[-1]+H[n-1])
mind = inf
for i in range(m):
    a = W[i]

    idx = bisect.bisect(H, a)

    for t in [idx-1, idx]:
        if t % 2 == 0:
            if t > 0:
                ans = abs(H[t]-W[i]) + rest_m[-1] - \
                    rest_m[t//2] + rest_x[t//2 - 1]
            else:
                ans = abs(H[0]-W[i]) + rest_m[-1] - H[0]
        else:
            if t < n:
                ans = abs(H[t]-W[i]) + abs(H[t-1]-H[t+1]) + \
                    rest_m[-1] - rest_m[(t+1)//2] + rest_x[(t-1)//2 - 1]
            else:
                ans = abs(H[n-1]-W[i]) + rest_x[-2]

        mind = min(mind, ans)

print(mind)
