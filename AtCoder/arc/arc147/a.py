from collections import deque


def main():
    N = int(input())
    A = sorted(map(int, input().split()))
    A = deque(A)
    cnt = 0
    while len(A) >= 2:
        cnt += 1
        aj, ai = A.popleft(), A.pop()
        ai %= aj
        A.appendleft(aj)
        if ai != 0:
            A.appendleft(ai)
    print(cnt)


if __name__ == '__main__':
    main()
