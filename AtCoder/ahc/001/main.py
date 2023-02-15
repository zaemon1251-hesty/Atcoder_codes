"""
Summary
1. Initialize ans and p.
    • ans[i] = [x,y,x+1,y+1]
    • p[i] = 1.0 - (1.0 - 1.0/r)**2
2. Expand all advertisements.
    Repeat 2.1 ~ 2.3.
    2.1 Choose an advertisement.
        • Give priority to advertisements whose p are low.
    2.2 Choose a direction.
        • Up, Down, Left or Right
    2.3 Expand the advertisement in the direction.
        • Don't expand too long.
3. Anneal the answer.
    Repeat 3.1 ~ 3.2.
    3.1 Update a part of the advertisements.
        • Choose 2 ~ 4 advertisements.
    3.2 Update an advertisement.
        • Choose 1 advertisement.
"""

from random import random, randrange, sample, shuffle, choice, uniform
from bisect import bisect_left
from itertools import accumulate
from math import sqrt
from time import time
from sys import stdin
input = stdin.readline

size = 10000
time_limit = 4.6


def receive_inputs():
    n = int(input())
    xyr = [tuple(map(int, input().split())) for _ in range(n)]
    return n, xyr


def overlap(i, j):
    return i[0] < j[2] and i[1] < j[3] and j[0] < i[2] and j[1] < i[3]


def overlap_index(ans, i):
    res = []
    for j in range(len(ans)):
        if i == j:
            continue
        if overlap(ans[i], ans[j]):
            res.append(j)
    return res


def main(n, xyr):
    start = time()

    def stopper(limit=time_limit):
        return time() - start < limit

    ans = [[x, y, x + 1, y + 1] for x, y, r in xyr]

    p = [0.0] * n
    for i in range(n):
        x, y, r = xyr[i]
        a, b, c, d = ans[i]
        s = (c - a) * (d - b)
        p[i] = 1.0 - (1.0 - min(r, s) / max(r, s))**2

    done = [[0] * 4 for _ in range(n)]

    def expand(i, direction, maximum=32):
        x, y, r = xyr[i]
        a, b, c, d = ans[i]
        s = (c - a) * (d - b)
        if direction % 2:
            if r - (c - a) // 2 <= s:
                return
            maximum = min(maximum, (r - s + (c - a) // 2) // (c - a))
        else:
            if r - (d - b) // 2 <= s:
                return
            maximum = min(maximum, (r - s + (d - b) // 2) // (d - b))

        if direction // 2:
            if ans[i][direction] == size:
                done[i][direction] = 1
                return
            limit = size
        else:
            if ans[i][direction] == 0:
                done[i][direction] = 1
                return
            limit = 0

        for j in range(n):
            if i == j:
                continue
            aj, bj, cj, dj = ans[j]
            flags = [a < cj, b < dj, aj < c, bj < d]
            flags.pop(direction)
            if all(flags):
                if direction // 2:
                    limit = min(limit, ans[j][direction - 2])
                else:
                    limit = max(limit, ans[j][direction + 2])

        if direction // 2:
            if limit <= ans[i][direction] + maximum:
                done[i][direction] = 1
                ans[i][direction] = limit
            else:
                done[i][direction] = 0
                ans[i][direction] = ans[i][direction] + maximum
        else:
            if ans[i][direction] - maximum <= limit:
                done[i][direction] = 1
                ans[i][direction] = limit
            else:
                done[i][direction] = 0
                ans[i][direction] = ans[i][direction] - maximum

        a, b, c, d = ans[i]
        s = (c - a) * (d - b)
        p[i] = 1.0 - (1.0 - min(r, s) / max(r, s))**2

    indexes = list(range(n))
    cumsum = list(accumulate([1 - p[i] + 1e-4 for i in indexes]))
    directions = list(range(4))

    def choose_index():
        return indexes[bisect_left(cumsum, uniform(0.0, cumsum[-1]))]

    def choose_direction(i):
        shuffle(directions)
        for direction in directions:
            if not done[i][direction]:
                return direction

    def update(i, direction):
        expand(i, direction)
        x, y, r = xyr[i]
        a, b, c, d = ans[i]
        if r - max(c - a, d - b) // 2 <= (c - a) * (d - b) or all(done[i]):
            indexes.remove(i)
            return True
        return False

    # greedy
    while indexes:
        i = choose_index()
        direction = choose_direction(i)
        if update(i, direction):
            cumsum = list(accumulate([1 - p[i] + 1e-4 for i in indexes]))

    indexes = list(range(n))

    def improve(i, direction, scheduler):
        if direction // 2:
            if ans[i][direction] == size:
                return
            ans[i][direction] += 1
            j = overlap_index(ans, i)
            ans[i][direction] -= 1
        else:
            if ans[i][direction] == 0:
                return
            ans[i][direction] -= 1
            j = overlap_index(ans, i)
            ans[i][direction] += 1

        if not 0 < len(j) < 4:
            return
        j = [i] + j
        old_ans = []
        old_p = []
        for ij in j:
            old_ans.append(ans[ij])
            old_p.append(p[ij])
            x, y, r = xyr[ij]
            ans[ij] = [x, y, x + 1, y + 1]
        i_or_j = j.copy()
        shuffle(i_or_j)
        for ij in i_or_j:
            shuffle(directions)
            for new_direction in directions:
                expand(ij, new_direction, maximum=size)
        delta = sum([p[ij] for ij in j]) - sum(old_p)
        if scheduler(delta):
            return
        for idx, ij in enumerate(j):
            ans[ij] = old_ans[idx]
            p[ij] = old_p[idx]

    def improve_all(scheduler=lambda x: 0.0 < x):
        shuffle(indexes)
        for i in indexes:
            if 0.99 < p[i]:
                continue
            shuffle(directions)
            for direction in directions:
                improve(i, direction, scheduler)

    def shuffle_directions(scheduler=lambda x: 0.0 < x):
        shuffle(indexes)
        for i in indexes:
            x, y, r = xyr[i]
            old_ans = ans[i]
            old_p = p[i]
            ans[i] = [x, y, x + 1, y + 1]
            shuffle(directions)
            for direction in directions:
                expand(i, direction, maximum=size)
            delta = p[i] - old_p
            if scheduler(delta):
                continue
            ans[i] = old_ans
            p[i] = old_p

    # annealing
    t0 = 1e-1
    t1 = 1e-3
    annealing_start = time()
    lap = 0
    while stopper(time_limit):
        t = (time() - annealing_start) / (start + time_limit - annealing_start)
        T = pow(t0, 1.0 - t) * pow(t1, t)

        def scheduler(delta):
            return 0.0 < delta or random() < pow(2.0, delta / T)

        improve_all(scheduler)
        shuffle_directions(scheduler)

        # if lap % 10 == 0:
        #print(lap, 50*sum(p)/n, T)
        lap += 1

    return ans


n, xyr = receive_inputs()
ans = main(n, xyr)
print(*[' '.join(map(str, i)) for i in ans], sep='\n')


### DEBUG ###
def checker(n, xyr, ans, output=True):
    assert len(ans) == n
    for i in range(n):
        x, y, r = xyr[i]
        ai, bi, ci, di = ans[i]
        assert 0 <= ai <= x < ci <= size
        assert 0 <= bi <= y < di <= size
        for j in range(n):
            if i == j:
                continue
            if overlap(ans[i], ans[j]):
                print('NG')
                print(xyr[i])
                print(ans[i])
                print(xyr[j])
                print(ans[j])
                return False
    if output:
        print('OK')
    return True


def visualizer(n, xyr, ans, p):
    from PIL import Image, ImageDraw

    img = Image.new('RGB', (size, size), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    for abcd in ans:
        draw.rectangle(
            abcd, fill=(
                randrange(
                    32, 224), randrange(
                    32, 224), randrange(
                    32, 224)))

    for i in range(n):
        x, y, r = xyr[i]
        r = sqrt(r) / 20
        a = max(0, x - r)
        b = max(0, y - r)
        c = min(size, x + r)
        d = min(size, y + r)
        draw.ellipse((a, b, c, d), fill=(
            int(p[i] * 255), int(p[i] * 255), int(p[i] * 255)))

        a, b, c, d = ans[i]
        draw.line(((x, y), ((a + c) // 2, (b + d) // 2)),
                  fill=(255, 255, 255), width=10)

    img.save('out.jpg')
    print('Image file "out.jpg" was created.')


def score_calculater(n, xyr, ans, output=True):
    p = [0.0] * n
    for i in range(n):
        x, y, r = xyr[i]
        a, b, c, d = ans[i]
        if not (a <= x < c and b <= y < d):
            continue
        s = (c - a) * (d - b)
        p[i] = 1 - (1 - min(r, s) / max(r, s))**2
    if output:
        print('score:', sum(p) * 50.0 / n)
    return p


def debug(n, xyr, ans):
    p = score_calculater(n, xyr, ans)
    visualizer(n, xyr, ans, p)
    checker(n, xyr, ans)


def generator():
    n = round(50 * 4**random())
    while True:
        xy = [(randrange(10**4), randrange(10**4)) for _ in range(n)]
        if len(set(xy)) == n:
            break
    sampled = sample(range(1, 10**8), n - 1)
    sampled.sort()
    sampled.append(10**8)
    sampled.append(0)
    xyr = [(0, 0, 0)] * n
    for i in range(n):
        xyr[i] = (xy[i][0], xy[i][1], sampled[i] - sampled[i - 1])
    return n, xyr


def tester(repeat=10):
    score = 0.0
    for _ in range(repeat):
        n, xyr = generator()
        start = time()
        ans = main(n, xyr)
        print(_, n, time() - start)
        if not checker(n, xyr, ans, output=False):
            return
        score += sum(score_calculater(n, xyr, ans, output=False)) * 50.0 / n
    print('score:', score / repeat)


def visualize_random_sample():
    n, xyr = generator()
    ans = main(n, xyr)
    visualizer(n, xyr, ans, score_calculater(n, xyr, ans, output=True))


# debug(n, xyr, ans)
# tester()
# visualize_random_sample()
