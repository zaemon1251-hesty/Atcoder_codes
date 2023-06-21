#!/bin/python3
from __future__ import annotations
import math
import os
import random
import re
import sys
import heapq

inf = 10e9
#
# Complete the 'calculateProfit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER x
#  3. INTEGER y
#  4. INTEGER z
#


def calculateProfit(arr: list[int], x: int, y: int, z: int) -> int:
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    profits = [0] * (n + 1)
    max_profits = [0] * (n + 1)
    queue = []

    for i in range(1, n + 1):
        if i >= 1:
            profit = prefix_sum[i] - prefix_sum[i - 1]
            heapq.heappush(queue, (-profit, 1))
            while len(queue) > 0 and queue[0][1] > x:
                heapq.heappop(queue)
            profits[i] = -queue[0][0] if len(queue) > 0 else 0

        if i >= 2:
            profit = prefix_sum[i] - prefix_sum[i - 2]
            heapq.heappush(queue, (-profit, 2))
            while len(queue) > 0 and queue[0][1] > x + y:
                heapq.heappop(queue)
            profits[i] = max(profits[i], -queue[0][0] if len(queue) > 0 else 0)

        if i >= 3:
            profit = prefix_sum[i] - prefix_sum[i - 3]
            heapq.heappush(queue, (-profit, 3))
            while len(queue) > 0 and queue[0][1] > x + y + z:
                heapq.heappop(queue)
            profits[i] = max(profits[i], -queue[0][0] if len(queue) > 0 else 0)

        max_profits[i] = max(max_profits[i - 1], profits[i])

    return max_profits[n]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    x = int(input().strip())

    y = int(input().strip())

    z = int(input().strip())

    result = calculateProfit(arr, x, y, z)

    fptr.write(str(result) + "\n")

    fptr.close()
