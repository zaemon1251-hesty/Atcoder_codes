def main():
    N = list(input())
    cols = [[6], [3], [1, 7], [0, 4], [2, 8], [5], [9]]
    if N[0] != "0":
        print("No")
        exit()

    colstand = [any(N[j] == "1" for j in pins) for pins in cols]

    for i in range(6):
        for j in range(i + 1, 7):
            if colstand[i] & colstand[j] & any(
                    not colstand[k] for k in range(i + 1, j)):
                print("Yes")
                exit()
    print("No")


if __name__ == '__main__':
    main()
