from email.policy import default
import sys
from collections import defaultdict, deque
from typing import Deque, Dict

M = 0
K = 0


menus = {}
orders = []

q: Deque[str] = deque([])


class Seat:
    def __init__(self, id):
        self.id = id
        self.total = 0


class Kitchen:
    def __init__(self, k):
        self.k = k


class Microwave:
    def __init__(self):
        self.available = True


class Menu:
    def __init__(self, id, zaiko, price):
        self.id = id
        self.zaiko = zaiko
        self.price = price


class Order:
    def __init__(self, menu_id, seat_id, num):
        self.menu_id = menu_id
        self.seat_id = seat_id
        self.num = num


def runner():
    while q:
        n = int(q.popleft())
        if n == 1:
            step1()
        elif n == 2:
            step2()
        elif n == 3:
            step3()
        elif n == 4:
            step4()
        else:
            raise Exception("invalid query number")


def step1():
    menu_num = int(q.popleft())

    for _ in range(menu_num):
        d, s, p = map(int, q.popleft().split())
        menus[d] = {"zaiko": s, "price": p}

    # buf = deque([])

    while q and not q[0].isnumeric():
        _, t, d, n = map(str, q.popleft().split())
        t, d, n = int(t), int(d), int(n)

        if d in menus and menus[d]["zaiko"] < n:
            print("sold out {}".format(t))
            continue

        menus[d]["zaiko"] -= n
        orders.append((t, d, n))
        for _ in range(n):
            print("received order {} {}".format(t, d))

    # print(*buf, sep="\n")


def step2():
    menu_num, micro_num = map(int, q.popleft().split())

    heating_orders = [None] * micro_num
    waiting_orders = deque([])

    for _ in range(menu_num):
        d, s, p = map(int, q.popleft().split())
        menus[d] = {"zaiko": s, "price": p}

    while q and not q[0].isnumeric():
        query = q.popleft()
        if query[0] == "r":
            _, _, t, d = map(str, query.split())
            t, d = int(t), int(d)
            order = {"seat_id": t, "menu_id": d}
            try:
                # bottle neck
                mw_id = heating_orders.index(None)
                heating_orders[mw_id] = order
                print(order["menu_id"])
            except Exception:
                waiting_orders.append(order)
                print("wait")

        elif query[0] == "c":
            _, d = map(str, query.split())
            d = int(d)

            idx = None
            # bottle neck
            for i, ho in enumerate(heating_orders):
                if ho and ho["menu_id"] == d:
                    idx = i
                    break
            if idx is None:
                print("unexpected input")
                continue

            if waiting_orders:
                order = waiting_orders.popleft()
                heating_orders[idx] = order
                print("ok {}".format(order["menu_id"]))
            else:
                heating_orders[idx] = None
                print("ok")

        else:
            raise Exception("unexpected query")


def step3():
    menu_num = int(q.popleft())

    order_seats = []

    for _ in range(menu_num):
        d, s, p = map(int, q.popleft().split())
        menus[d] = {"zaiko": s, "price": p}

    while q and not q[0].isnumeric():
        query = q.popleft()

        if query[0] == "r":
            _, _, t, d = map(str, query.split())
            t, d = int(t), int(d)
            order_seats.append((t, d))

        elif query[0] == "c":
            _, d = map(str, query.split())
            d = int(d)

            idx = None
            new_orders = []

            # bottle neck
            for i, o_seat in enumerate(order_seats):
                if o_seat and o_seat[1] == d:
                    idx = i
                    break
                new_orders.append(o_seat)

            if idx is not None:
                print("ready {} {}".format(*order_seats[idx]))
                order_seats[idx] = None
            else:
                print("i,d = ", idx, d)

        else:
            raise Exception("unexpected query")


def step4():
    menu_num = int(q.popleft())

    seats: Dict[int, Dict[int, int]] = {}
    seats_total: Dict[int, int] = {}

    for _ in range(menu_num):
        d, s, p = map(int, q.popleft().split())
        menus[d] = {"zaiko": s, "price": p}

    while q and not q[0].isnumeric():
        query = q.popleft()
        if "recieved" in query:
            _, _, t, d = map(str, query.split())
            t, d = int(t), int(d)

            if t not in seats:
                seats[t] = {}

            seats[t][d] = seats[t].get(d, 0) + 1

        elif "ready" in query:
            _, t, d = map(str, query.split())
            t, d = int(t), int(d)

            if t not in seats or d not in seats:
                continue

            seats[t][d] -= 1

            seats_total[t] = seats_total.get(t, 0) + menus[d]["price"]

        elif "check" in query:
            _, t = map(str, query.split())
            t = int(t)
            if t in seats:
                if any(d != 0 for d in seats[t].values()):
                    print("please wait")
                else:
                    print(seats_total[t])
                    seats.pop(t)
                    seats_total.pop(t)
            else:
                # 注文無し
                print(0)


def main():
    # run this program
    runner()


if __name__ == '__main__':
    for l in sys.stdin:
        q.append(l.rstrip('\r\n'))
    main()
