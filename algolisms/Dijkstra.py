# ダイクストラ
from heapq import heappush, heappop
from typing import List

Vertex: List[int]
Graph: List[List[int]]

inf = 10e9
v, e, r = map(int, input().split())
G: Graph = [[] for _ in range(v)]

for i in range(e):
    st, en, w = map(int, input().split())
    G[st].append((en, w))

short = [inf] * v
short[r] = 0
todo = [(short[r], r)]

while todo:
    dista, dd = heappop(todo)
    if dista > short[dd]:
        continue  # 同じ始点と終点を持ち、重みだけが違う辺のうち、必要ない方をスキップする
    for to, weight in G[dd]:
        if short[to] > weight + short[dd]:
            short[to] = weight + short[dd]
            heappush(todo, (short[to], to))

for i in range(v):
    if short[i] != inf:
        print(short[i])
    else:
        print("INF")
