from itertools import accumulate


def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = accumulate(A)
    S = list(S)
    _max = 0
    t = 0
    ans = []
    for i in range(N):
        ans.append(t+_max)
        t += S[i]
        _max = max(_max, S[i])
        ans.append(t)
    print(max(ans))


if __name__ == '__main__':
    main()
