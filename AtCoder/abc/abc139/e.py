from collections import deque


def main():
    N = int(input())
    Q = [deque(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
    buf = set()
    for cu in range(N):
        to = Q[cu][0]
        if Q[to][0] == cu:
            buf.add((min(cu, to), max(cu, to)))

    ans = 0
    while buf:
        ans += 1
        newbuf = set()
        for a, b in buf:
            Q[a].popleft()
            Q[b].popleft()

            if Q[a]:
                cu = Q[a][0]
                if Q[cu] and Q[cu][0] == a:
                    newbuf.add((min(a, cu), max(a, cu)))

            if Q[b]:
                cu = Q[b][0]
                if Q[cu] and Q[cu][0] == b:
                    newbuf.add((min(b, cu), max(b, cu)))
        buf = newbuf

    if any(Q[i] for i in range(N)):
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
