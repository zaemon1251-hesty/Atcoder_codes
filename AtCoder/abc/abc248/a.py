def main():
    N = set(input())
    for i in range(10):
        if str(i) not in N:
            print(i)
            exit()


if __name__ == '__main__':
    main()
