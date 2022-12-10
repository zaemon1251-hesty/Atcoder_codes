def main():
    N = int(input())
    x = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if -abs(x[j][0] - x[i][0]) <= (x[j][1] - x[i][1]) <= abs(x[j][0] - x[i][0]):
                ans += 1
    print(ans)



if __name__ == '__main__':
    main()