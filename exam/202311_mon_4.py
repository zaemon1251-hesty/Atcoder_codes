import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    a, b, n = map(int, lines[0].split())
    ok = 10**12
    ng = 0
    while abs(ok - ng) > 1:
        cen = (ok + ng) // 2
        if a * (cen + 1) + b * count_numbers_with_seven(cen) >= n:
            ok = cen
        else:
            ng = cen
    print(ok)


def count_numbers_with_seven(d: int) -> int:
    d_str = str(d)
    length = len(d_str)
    total_count = 0

    # length-1桁以下の数の7の個数を数える
    total_count += 10 ** (length - 2) - 9 ** (length - 2)
    # 2桁目以降の各桁の数値までの7の個数を数える
    for i in range(length):
        digit = int(d_str[i])

        for j in range(digit):
            if j == 0 and i == 0:
                continue
            if j == 7:
                total_count += 10 ** (length - i - 1)
            else:
                total_count += 10 ** (length - i - 1) - 9 ** (length - i - 1)

        if digit == 7:
            total_count += int(d_str[i + 1 :]) + 1 if i + 1 < length else 1
            break

    return total_count


def _count_numbers_with_seven(d: int) -> int:
    def count_sevens_in_position(length: int, pos: int) -> int:
        """Counts the numbers containing 7 at a specific position."""
        return 9 ** (length - pos) * 8 ** (pos - 1)

    d_str = str(d)
    length = len(d_str)
    total_count = 0

    # Count numbers with 7 in each position
    for pos in range(1, length):
        total_count += count_sevens_in_position(length, pos)

    # Handle the most significant digits up to d
    for i, digit in enumerate(d_str):
        digit = int(digit)
        if digit > 7:
            total_count += count_sevens_in_position(length - i, 1)
        elif digit == 7:
            total_count += int(d_str[i + 1 :]) + 1 if i + 1 < length else 1
            break

    return total_count


# Example usage
if __name__ == "__main__":
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip("\r\n"))
    main(lines)
