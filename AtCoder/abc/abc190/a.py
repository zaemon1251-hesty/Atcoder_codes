def main():
    A, B, C = map(int, input().split())
    t = [A, B]
    name = ["Takahashi", "Aoki"]
    while True:
        t[C] -= 1
        if t[C] < 0:
            print(name[1 - C])
            exit()
        C = 1 - C


if __name__ == "__main__":
    main()
