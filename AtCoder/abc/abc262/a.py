def main():
    Y = int(input())
    for i in range(Y, 3020):
        if i % 4 == 2:
            print(i)
            exit()


if __name__ == '__main__':
    main()
