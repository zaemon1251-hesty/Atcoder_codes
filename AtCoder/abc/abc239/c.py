def main():
    x1, y1, x2, y2 = map(int, input().split())
    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    for i in range(8):
        for j in range(8):
            nx1, ny1 = x1+dx[i], y1+dy[i]
            nx2, ny2 = x2+dx[j], y2+dy[j]
            if nx1 == nx2 and ny1 == ny2:
                print("Yes")
                exit()
    print("No")


if __name__ == '__main__':
    main()
