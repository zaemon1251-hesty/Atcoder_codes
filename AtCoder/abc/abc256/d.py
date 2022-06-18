def merger(intervals):
    intervals.sort(key=lambda interval: interval[0])
    merged = [intervals[0]]
    for w in intervals:
        if w[0] > merged[-1][1]:
            merged.append(w)
        elif w[1] > merged[-1][1]:
            merged[-1][1] = w[1]
    return merged


def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    merged = merger(A)
    for m in merged:
        print(*m)


if __name__ == '__main__':
    main()
