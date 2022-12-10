def main():
    N, Q = map(int, input().split())
    S = list(input())
    head, tail = 0, N - 1
    for _ in range(Q):
        q, x = map(int, input().split())
        if q == 1:
            head = (N + tail - x + 1) % N
            tail = (N + tail - x) % N
        else:
            print(S[(head + x - 1) % N])


if __name__ == '__main__':
    main()
