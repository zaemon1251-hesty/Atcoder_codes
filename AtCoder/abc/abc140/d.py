def main():
    N, K = map(int, input().split())
    S = list(input())
    prev = ""
    gr = []
    for i in range(N):
        if S[i] == prev:
            gr[-1] += 1
        else:
            gr.append(0)
        prev = S[i]
    gl = len(gr)
    for k in range(K):
        if gl >= 3:
            gl -= 2
        elif gl == 2:
            gl = 1
    print(N - gl)

    l, r = 0, 0


if __name__ == '__main__':
    main()
