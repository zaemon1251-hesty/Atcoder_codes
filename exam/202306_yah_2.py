from __future__ import annotations
import sys
from collections import deque


def parse(lines: deque[str]):
    try:
        N = int(lines.popleft())
        tmpl = lines.popleft().split()
        n = int(lines.popleft())
    except ValueError:
        raise ValueError("Invalid input: N, tmpl, n")

    infomations = []
    for trhksk_i in range(n):
        try:
            trhksk_infomation = {}
            li = int(lines.popleft())
            for _ in range(li):
                a, b = lines.popleft().split()
                trhksk_infomation[a] = b
            infomations.append(trhksk_infomation)
        except ValueError:
            raise ValueError("Invalid input: trhksk_infomation number {}".format(trhksk_i))

    return N, tmpl, infomations


def main(lines):
    N, tmplates, infomations = parse(lines)
    for trhksk_infomation in infomations:
        response = []
        for word in tmplates:
            if word.startswith("#"):
                if word in trhksk_infomation:
                    response.append(trhksk_infomation[word])
                else:
                    break
            else:
                response.append(word)
        else:
            print(" ".join(response))
            # 全ての置換情報の置き換えに成功している場合は、次のtrhksk_infomationに進む
            continue
        # ここまで来たら、breakされている。
        # つまり、テンプレート内全ての置換対象を置き換えることができなかった
        print("Error: Lack of data")


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(deque(lines))
