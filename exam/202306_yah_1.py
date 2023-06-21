from __future__ import annotations
import sys


def parse(line: list[str]):
    n_raw, *m_raw = line[0].split()
    menber_heights_raw = map(lambda x: x.split(), line[1:])

    return int(n_raw), list(map(int, m_raw)), list(menber_heights_raw)


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    n, m, menber_weights = parse(lines)
    uniform_size = {"S": [], "M": [], "L": [], "X": []}
    for i in range(n):
        name, d = menber_weights[i]
        d = int(d)
        if m[0] <= d < m[1]:
            uniform_size["S"].append(name)
        elif m[1] <= d < m[2]:
            uniform_size["M"].append(name)
        elif m[2] <= d < m[3]:
            uniform_size["L"].append(name)
        else:
            uniform_size["X"].append(name)

    for size in ["S", "M", "L", "X"]:
        print(size + ":")
        for name in uniform_size[size]:
            print(name)


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
