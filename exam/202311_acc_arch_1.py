from __future__ import annotations
import sys
from itertools import combinations


def main(lines):
    user_number, relationship_number, relationship_edges = parse_args(lines)
    # relationships[i] = ユーザーi がフォローしているユーザーの集合
    relationships = preprocess(user_number, relationship_edges)
    user_cyclic = solve(user_number, relationship_number, relationships)
    print(user_cyclic)


def preprocess(user_number: int, relationship_edges: list[tuple[int, int]]) -> list[list[int]]:
    graph = [set() for _ in range(user_number)]
    for u, v in relationship_edges:
        graph[u - 1].add(v - 1)
    return graph


def solve(n: int, m: int, G: list[list[int]]) -> int:
    result = 0
    for i, j, k in combinations(range(n), 3):
        if j in G[i] and k in G[j] and i in G[k] or k in G[i] and i in G[j] and j in G[k]:
            result += 1
    return result


def parse_args(lines) -> tuple[int, int, list[tuple[int, int]]]:
    user_number, relationship_number = map(int, lines[0].split())
    relationship_edges = []
    for line in lines[1:]:
        relationship_edges.append(tuple(map(int, line.split())))
    return user_number, relationship_number, relationship_edges


if __name__ == "__main__":
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip("\r\n"))
    main(lines)
