# AC x 3
# WA x 1
# TLE x 2
# RE x 0

from typing import Counter


N = int(input())
S = [input() for _ in range(N)]
S = Counter(S)

for res in ["AC", "WA", "TLE", "RE"]:
    print("%s x %s" % (res, S[res]))
