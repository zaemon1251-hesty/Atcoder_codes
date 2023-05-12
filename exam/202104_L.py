# https://engineering.linecorp.com/ja/blog/commentary-of-coding-test-2021

import re
from enum import IntEnum, auto
from collections import deque

# 運賃計算に必要な定数
INITIAL_FARE = 400    # 初乗り運賃
SHORT_DISTANCE_FARE_RATE = 40  # 短距離運賃の加算額（400mごと）
LONG_DISTANCE_FARE_RATE = 40  # 長距離運賃の加算額（350mごと）
LOW_SPEED_FARE = 40   # 低速走行料金の加算額
LOW_SPEED_TIME_THRESHOLD = 45   # 低速走行料金の適用閾値（秒）
NIGHTTIME_FARE_RATE = 1.3   # 深夜料金の割増率（30%）
PEAKTIME_FARE_RATE = 1.5   # ピークタイム料金の割増率（50%）

FREE_THERESHOLD = 10000
DISTANCE_THERESHOLD = 102000  # 短距離運賃の適用閾値（0.1メートル=1）

hour_base = 3600 * 1000
minute_base = 60 * 1000


class DistanceState(IntEnum):
    free: int = auto()
    short: int = auto()
    long: int = auto()


def convert_to_milliseconds(dt: list) -> int:
    dt = list(map(int, dt))
    milliseconds = (dt[0] * 3600 + dt[1] * 60 +
                    dt[2]) * 1000 + dt[3]
    return milliseconds


def is_midnight(time: int):
    time %= 24 * hour_base
    return time < 6 * hour_base


def is_peak(time: int):
    time %= 24 * hour_base
    return 7 * hour_base <= time < 9 * hour_base + 30 * minute_base or \
        18 * hour_base <= time < 24 * hour_base


def process_file(input_file_path) -> deque:
    # 乗車履歴を読み込んで、運賃を計算する関数

    prev_time = None  # 前回の時刻

    res: deque = deque([])

    # 入力ファイルを読み込む
    try:
        with open(input_file_path, "r") as f:
            records = f.readlines()
    except BaseException:
        raise RuntimeError("エラー：ファイルが読み込めません。")

    if len(records) < 2:
        raise ValueError

    # 入力データのバリデーションチェック
    for i, record in enumerate(records):
        # 時間と距離を取得
        time_str, distance_str = record.strip().split()

        # 初乗りの距離が0かチェック
        if i == 0 and distance_str != "0.0":
            raise ValueError

        # 時間と距離のフォーマットチェック
        print(time_str, distance_str)
        if len(time_str) != 12 or not time_str[:2].isdigit() or not time_str[3:5].isdigit(
        ) or not time_str[6:8].isdigit() or not time_str[9:].isdigit() or not distance_str.replace(".", "").isdigit():
            raise ValueError

        time_dt = re.split(r"[:\.]", time_str)

        current_time = convert_to_milliseconds(time_dt)

        _is_midnight = is_midnight(current_time)
        _is_peak = is_peak(current_time)
        distance_diff = int(distance_str.replace(".", ""))

        # 45秒を超えていないかどうかチェック
        if prev_time is not None and current_time - prev_time > 45 * 1000:
            raise ValueError

        if prev_time is None:
            time_diff = 0
        else:
            time_diff = current_time - prev_time

        res.append([time_diff, distance_diff, _is_midnight, _is_peak])

        prev_time = current_time

    return res


def get_price_regard_distance_time(
        distance: int,
        distance_state: DistanceState,
        is_midnight: bool,
        is_peak: bool):

    assert is_midnight is False or is_peak is False

    _price = 0.0

    if distance_state == DistanceState.free:
        _distance_mod = 0
        pass
    elif distance_state == DistanceState.short:
        _price += SHORT_DISTANCE_FARE_RATE * \
            (distance // 4000)
        _distance_mod = distance % 4000
    else:
        _price += SHORT_DISTANCE_FARE_RATE * \
            (distance // 3500)
        _distance_mod = distance % 3500

    if is_midnight:
        _price *= NIGHTTIME_FARE_RATE
    elif is_peak:
        _price *= PEAKTIME_FARE_RATE

    return round(_price), _distance_mod


def get_price_regard_initial_fare(
        distance: int, is_midnight: bool, is_peak: bool):

    assert distance == 0
    assert is_midnight is False or is_peak is False

    _price: float = INITIAL_FARE

    if is_midnight:
        _price *= NIGHTTIME_FARE_RATE
    elif is_peak:
        _price *= PEAKTIME_FARE_RATE

    return round(_price)


def calc_price(que: deque):

    # 運賃計算のため変数
    total_distance = 0    # 累計距離
    distance_mod = 0    # 累計距離の余剰 (mod 1000 or 3500 or 4000)
    total_fare = 0.0    # 累計運賃
    low_speed_time = 0    # 累積低速走行時間 (mod 45 * 1000)
    fare_time = 0    # 運賃を計算するための時間
    state = DistanceState.free   # 現在の距離状態

    def process_first_ride(time, distance, is_midnight, is_peak):
        # 乗車履歴の最初のレコードを処理する関数
        nonlocal total_distance, total_fare, low_speed_time, fare_time, distance_mod

        assert distance == 0

        total_fare += get_price_regard_initial_fare(
            distance, is_midnight, is_peak)

        low_speed_time += time if (360 * distance <= 10 * time) else 0

        fare_time += time

    def process_meter(time, distance, is_midnight, is_peak):
        # 乗車履歴の距離を処理する関数
        nonlocal total_distance, total_fare, low_speed_time, fare_time, state, distance_mod

        print(time, distance, is_midnight, is_peak)

        total_distance += distance

        if DISTANCE_THERESHOLD <= total_distance:
            state = DistanceState.long
        elif FREE_THERESHOLD <= total_distance:
            state = DistanceState.short

        distance_diff = distance + distance_mod

        price, distance_mod = get_price_regard_distance_time(
            distance_diff, state, is_midnight, is_peak)

        total_fare += price

        low_speed_time += time if (360 * distance <= 10 * time) else 0

        ope, low_speed_time = divmod(low_speed_time, 45 * 1000)
        total_fare += ope * LOW_SPEED_FARE
        fare_time += time

    time, distance, is_midnight, is_peak = que.popleft()
    process_first_ride(time, distance, is_midnight, is_peak)

    while que:
        time, distance, is_midnight, is_peak = que.popleft()
        process_meter(time, distance, is_midnight, is_peak)

    assert total_distance > 0

    return total_fare


def main():
    import os
    from pathlib import Path
    file_path = Path(os.path.dirname(__file__)) / "input.txt"
    que = process_file(file_path)
    result = calc_price(que)
    return result


if __name__ == "__main__":
    print(main())
