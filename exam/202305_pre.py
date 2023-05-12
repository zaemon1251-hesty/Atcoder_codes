from itertools import combinations, product
from typing import List


def main():
    # Read input
    R, C = map(int, input().split())
    N = int(input())
    segments = []
    exist_x = [0, R]
    exist_y = [0, C]
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        segments.append((a, b, c, d))

        # add endpoints of the line
        exist_x.extend([a, c])
        exist_y.extend([b, d])

        # add Space adjacent to the line
        exist_x.extend([max(a - 1, 0), min(c + 1, R)])
        exist_y.extend([max(b - 1, 0), min(d + 1, C)])

    # compress
    x_to_i, i_to_x = compress_1d(exist_x)
    y_to_i, i_to_y = compress_1d(exist_y)

    # convert segments
    segments = [(x_to_i[a], y_to_i[b], x_to_i[c], y_to_i[d]) for a, b, c, d in segments]

    # Calculate and print the result
    r = len(x_to_i)
    c = len(y_to_i)

    result = calculate_largest_area(r, c, segments, i_to_x, i_to_y)
    print(result)


def compress_1d(A: List[int]):
    # compress 1d array
    setA = set(A)
    x_to_i = {x: i for i, x in enumerate(sorted(setA), 0)}
    i_to_x = {i: x for i, x in enumerate(sorted(setA), 0)}
    return x_to_i, i_to_x


def calculate_largest_area(r, c, segments, i_to_x, i_to_y):
    # Calculate the largest area
    largest_area = 0
    ac_combinations = combinations(range(r), 2)
    bd_combinations = combinations(range(c), 2)
    for (a, c), (b, d) in product(ac_combinations, bd_combinations):
        # Convert the index to the real value
        # and calculate the area
        real_a = i_to_x[a]
        real_b = i_to_y[b]
        real_c = i_to_x[c]
        real_d = i_to_y[d]
        area = (real_c - real_a) * (real_d - real_b)

        rect = (a, b, c, d)
        if area > largest_area:
            # Check if the area is valid
            valid = True
            for segment in segments:
                if line_intersects_rectangle(rect, segment):
                    valid = False
                    break
            if valid:
                largest_area = area

    return largest_area


def line_intersects_rectangle(rect, line):
    # Check if the line intersects any of the four sides of the rectangle
    rect_left, rect_bottom, rect_right, rect_top = rect
    x1, y1, x2, y2 = line

    if x1 == x2:
        # vertical line
        if not rect_left < x1 < rect_right:
            return False

        if rect_bottom <= y1 <= rect_top or rect_bottom <= y2 <= rect_top:
            # exclude the case where endpoint of the line is on
            # the edge of the rectangle
            if y2 == rect_bottom or y1 == rect_top:
                return False

            return True

    elif y1 == y2:
        # horizontal line
        if not rect_bottom < y1 < rect_top:
            return False

        if rect_left <= x1 <= rect_right or rect_left <= x2 <= rect_right:
            # exclude the case where endpoint　of the line is on
            # the edge of the rectangle
            if x2 == rect_left or x1 == rect_right:
                return False

            return True
    else:
        raise ValueError("The line is not vertical or horizontal.")

    # If there is no intersection, return False
    return False


if __name__ == "__main__":
    main()
