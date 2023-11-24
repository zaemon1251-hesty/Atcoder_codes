import sys
from string import ascii_lowercase
from itertools import product
from heapq import heappush, heappop
from collections import defaultdict


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    _ = int(lines[0])
    S = lines[1:]

    two_char = {a + b for a, b in product(ascii_lowercase, repeat=2)}

    suffix = {ab: [] for ab in two_char}
    prefix = {ab: [] for ab in two_char}
    dup = defaultdict(int)

    for s in S:
        if len(s) <= 2:
            continue
        suf = s[-2:]
        pre = s[:2]
        if suf == pre:
            dup[suf] = -len(s)
        heappush(suffix[suf], -len(s))
        heappush(prefix[pre], -len(s))

    result = -1
    for ab in two_char:
        if len(suffix[ab]) == 0 or len(prefix[ab]) == 0:
            continue
        if ab not in dup or not (dup[suf] == prefix[ab][0] == suffix[ab][0]):
            result_candidate = -prefix[ab][0] + -suffix[ab][0] - 2
            result = max(result, result_candidate)
        else:
            result_candidates = [-1]
            tmp_prefix_max = heappop(prefix[ab])
            if prefix[ab]:
                result_candidates.append(-prefix[ab][0] + -suffix[ab][0] - 2)
            heappush(prefix[ab], tmp_prefix_max)
            tmp_suffix_max = heappop(suffix[ab])
            if suffix[ab]:
                result_candidates.append(-prefix[ab][0] + -suffix[ab][0] - 2)
            heappush(suffix[ab], tmp_suffix_max)
            result = max(result, max(result_candidates))
    print(result)


if __name__ == "__main__":
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip("\r\n"))
    main(lines)
