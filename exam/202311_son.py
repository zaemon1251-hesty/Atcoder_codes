from __future__ import annotations
import sys
from collections import deque
from dataclasses import dataclass, field
from datetime import datetime
from math import sqrt
from enum import IntEnum, auto

"""
n m
MM-DD # n回繰り返す
レストランID x y # m 回繰り返す

YYYY-MM-DD HH:MM set_min レストランID 金額
YYYY-MM-DD HH:MM set_free レストランID 金額
YYYY-MM-DD HH:MM close_day レストランID 曜日もしくは祝日
YYYY-MM-DD HH:MM open_day レストランID 曜日もしくは祝日

YYYY-MM-DD HH:MM close_time レストランID HH:MM HH:MM
YYYY-MM-DD HH:MM open_time レストランID HH:MM HH:MM

YYYY-MM-DD HH:MM order レストランID 注文金額 x y

YYYY-MM-DD HH:MM calculate レストランID YYYY-MM-DD HH:MM YYYY-MM-DD HH:MM
"""

MAX_PRICE = 10**9


# 曜日の列挙型
class Week(IntEnum):
    Monday = 0
    Tuesday = auto()
    Wednesday = auto()
    Thursday = auto()
    Friday = auto()
    Saturday = auto()
    Sunday = auto()


STR_TO_WEEK = {
    "MON": Week.Monday,
    "TUE": Week.Tuesday,
    "WED": Week.Wednesday,
    "THU": Week.Thursday,
    "FRI": Week.Friday,
    "SAT": Week.Saturday,
    "SUN": Week.Sunday,
}


@dataclass
class Order:
    restaurant_id: str
    send_price: int
    order_price: int

    @property
    def get_total(self):
        return self.send_price + self.order_price


@dataclass(frozen=False)
class Restaurant:
    pos_x: int
    pos_y: int
    min_price: int = -MAX_PRICE
    free_price: int = MAX_PRICE
    close_day: list[Week] = field(default_factory=list)
    close_holiday: bool = False
    time_closing: list[bool] = field(default_factory=lambda: [False] * (24 * 60 + 1))
    sales: list[tuple(float, int)] = field(default_factory=list)
    sales_sorted: bool = True

    def calc_send_price(self, user_x: int, user_y: int):
        distance = sqrt((self.pos_x - user_x) ** 2 + (self.pos_y - user_y) ** 2)
        assert distance >= 0

        if distance < 100:
            return 300
        elif distance < 1000:
            return 600
        elif distance < 10000:
            return 900
        else:
            return 1200


HOLIDAY_NUM: int
RESTAURANT_NUM: int

RESTAURANTS: dict[str, Restaurant] = {}
HOLIDAYS: set[str] = set()


def main(lines: deque[str]):
    HOLIDAY_NUM, RESTAURANT_NUM = map(int, lines.popleft().split())

    # MM-DD の形式で休日が与えられる
    for _ in range(HOLIDAY_NUM):
        date_str = lines.popleft()
        HOLIDAYS.add(date_str)

    # レストランの情報を取得
    for _ in range(RESTAURANT_NUM):
        restaurant_id, x, y = lines.popleft().split()
        x = int(x)
        y = int(y)
        RESTAURANTS[restaurant_id] = Restaurant(pos_x=x, pos_y=y)

    # 各クエリを処理
    while lines:
        q = lines.popleft().split()
        date_str, time_str = q[0], q[1]
        q_type = q[2]
        restaurant_id = q[3]
        datetime_entity = datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M")
        process_query(q_type, datetime_entity, restaurant_id, q[4:])


def process_query(type: str, datetime_entity: datetime, restaurant_id: str, q: list[str]):
    def _order():
        assert len(q) == 3
        order_price, user_x, user_y = q
        order_price = int(order_price)
        user_x = int(user_x)
        user_y = int(user_y)
        process_order(datetime_entity, restaurant_id, order_price, user_x, user_y)

    def _set_min():
        assert len(q) == 1
        min_price = q[0]
        min_price = int(min_price)
        RESTAURANTS[restaurant_id].min_price = min_price

    def _set_free():
        assert len(q) == 1
        free_price = q[0]
        free_price = int(free_price)
        RESTAURANTS[restaurant_id].free_price = free_price

    def _close_day():
        assert len(q) == 1
        day = q[0]
        if day == "HOLIDAY":
            RESTAURANTS[restaurant_id].close_holiday = True
        else:
            if STR_TO_WEEK[day] in RESTAURANTS[restaurant_id].close_day:
                return
            RESTAURANTS[restaurant_id].close_day.append(STR_TO_WEEK[day])

    def _open_day():
        assert len(q) == 1
        day = q[0]
        if day == "HOLIDAY":
            RESTAURANTS[restaurant_id].close_holiday = False
        else:
            if STR_TO_WEEK[day] not in RESTAURANTS[restaurant_id].close_day:
                return
            RESTAURANTS[restaurant_id].close_day.remove(STR_TO_WEEK[day])

    def _close_time():
        assert len(q) == 2
        start, end = q
        if end == "00:00":
            end = "24:00"
        start_time = datetime.strptime(start, "%H:%M")
        end_time = datetime.strptime(end, "%H:%M")
        for i in range(start_time.hour * 60 + start_time.minute, end_time.hour * 60 + end_time.minute):
            RESTAURANTS[restaurant_id].time_closing[i] = True

    def _open_time():
        assert len(q) == 2
        start, end = q
        start_time = datetime.strptime(start, "%H:%M")
        if end == "00:00":
            end = "24:00"
        end_time = datetime.strptime(end, "%H:%M")
        for i in range(start_time.hour * 60 + start_time.minute, end_time.hour * 60 + end_time.minute):
            RESTAURANTS[restaurant_id].time_closing[i] = False

    def _calculate():
        assert len(q) == 4
        start_date, start_time, end_date, end_time = q
        start_timestamp = datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M")
        end_timestamp = datetime.strptime(f"{end_date} {end_time}", "%Y-%m-%d %H:%M")
        process_calc(datetime_entity, restaurant_id, start_timestamp, end_timestamp)

    type_to_func = {
        "set_min": _set_min,
        "set_free": _set_free,
        "close_day": _close_day,
        "open_day": _open_day,
        "close_time": _close_time,
        "open_time": _open_time,
        "order": _order,
        "calculate": _calculate,
    }

    return type_to_func[type]() if type in type_to_func else None


def process_order(datetime: datetime, restaurant_id: str, order_price: int, user_x, user_y):
    restaurant = RESTAURANTS.get(restaurant_id)
    assert restaurant is not None

    if (restaurant.close_holiday and datetime.strftime("%m-%d") in HOLIDAYS) or (
        datetime.weekday() in restaurant.close_day
    ):
        print(f"{datetime.strftime('%Y-%m-%d %H:%M')} ERROR CLOSED DAY")
        return

    if restaurant.time_closing[datetime.hour * 60 + datetime.minute]:
        print(f"{datetime.strftime('%Y-%m-%d %H:%M')} ERROR CLOSED TIME")
        return

    # 最低料金が設定されている場合は、最低料金を超えているかチェック
    if order_price <= restaurant.min_price:
        print(f"{datetime.strftime('%Y-%m-%d %H:%M')} ERROR INSUFFICIENT")
        return

    send_price = restaurant.calc_send_price(user_x, user_y)
    order = Order(
        restaurant_id=restaurant_id,
        send_price=send_price,
        order_price=order_price,
    )
    total = order.get_total
    sale = order_price

    # フリー料金が設定されている場合は、フリー料金を超えているかチェック
    if restaurant.free_price <= order_price:
        total -= send_price
        sale -= send_price

    # output: YYYY-MM-DD HH:MM 金額
    print(f"{datetime.strftime('%Y-%m-%d %H:%M')} {total}")

    # レストランの売り上げを記録
    restaurant.sales.append((datetime.timestamp(), sale))
    restaurant.sales_sorted = False
    RESTAURANTS.update({restaurant_id: restaurant})


def process_calc(datetime: datetime, restaurant_id: str, start: datetime, end: datetime):
    total_sales = 0

    restaurant = RESTAURANTS.get(restaurant_id)
    assert restaurant is not None

    if not restaurant.sales_sorted:
        restaurant.sales.sort(key=lambda x: x[0])
    start_timestamp = start.timestamp()
    end_timestamp = end.timestamp()

    current_index = 0
    while current_index < len(restaurant.sales) and restaurant.sales[current_index][0] < start_timestamp:
        current_index += 1

    while current_index < len(restaurant.sales) and restaurant.sales[current_index][0] < end_timestamp:
        total_sales += restaurant.sales[current_index][1]
        current_index += 1

    print(f"{datetime.strftime('%Y-%m-%d %H:%M')} SALES {total_sales}")

    restaurant.sales_sorted = False
    RESTAURANTS.update({restaurant_id: restaurant})


if __name__ == "__main__":
    lines = deque()
    for line in sys.stdin:
        lines.append(line.rstrip("\r\n"))
    main(lines)
