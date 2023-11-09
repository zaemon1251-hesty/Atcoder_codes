"""
イベントソート：i番目のサービスを利用し始める、k番目のサービスを利用し始める、等のイベントを日付順に並べかえる。
これを実現するために、eventに格納する要素は（イベントの日付, 何番目のイベントか）という二つの要素を持ったタプルにしておく
その後、eventをイベントの日付の小さい順に並べる。

costはi番目のサービスの価格
flagはi番目のサービスが現在利用されているかどうかを判定するための配列

"""
N, C = map(int, input().split())
event = []
cost = []
flag = [False] * N
price = 0
total = 0

for i in range(N):
    a, b, c = map(int, input().split())
    event.append((a, i))
    # bi日目まで利用するというのは、bi+1日目に利用をやめるという意味
    event.append((b + 1, i))
    cost.append(c)

event = sorted(event, key=lambda x: x[0])
# print(event)
time = event[0][0]
price = cost[event[0][1]]
flag[event[0][1]] = True


# イベントとイベントの間は値段の変化がないので、イベントからイベントまでの時間で発生した値段をまとめてtotalに足す
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
