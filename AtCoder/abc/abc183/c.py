from itertools import permutations


def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for path in permutations(list(range(1, N))):
        path = list(path)
        tmp = T[0][path[0]]
        for i in range(1, N-1):
            tmp += T[path[i-1]][path[i]]
        tmp += T[path[-1]][0]
        if tmp == K:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
