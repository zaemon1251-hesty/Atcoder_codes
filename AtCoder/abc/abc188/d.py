N, C = map(int, input().split())
event = []
cost = []
flag = [False] * N
price = 0
total = 0

for i in range(N):
    a, b, c = map(int, input().split())
    event.append((a, i))
    event.append((b + 1, i))
    cost.append(c)

event = sorted(event, key=lambda x: x[0])
# print(event)
time = event[0][0]
price = cost[event[0][1]]
flag[event[0][1]] = True
# total+=min(C,price)*index

for i in range(1, len(event)):
    pre_time = event[i - 1][0]
    time = event[i][0]
    term = time - pre_time
    # print(min(C,price)*term)
    total += min(C, price) * term

    if not flag[event[i][1]]:
        price += cost[event[i][1]]
        flag[event[i][1]] = True
    else:
        price -= cost[event[i][1]]

print(total)
