def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))


def sub():
    def calc(a, b):
        return sum(map(lambda x: (x[0] - x[1]) ** 2, zip(a, b)))

    m1, m2 = [9, 6, 7], [5, 5, 10]
    X = [[7.7, 5.8, 7.7], [10.1, 5.9, 7.3]]
    Y = [[4.9, 4.1, 7.9], [4.8, 5.0, 9.0], [6.4, 3.7, 8.0], [4.0, 5.2, 11.6]]
    m1 = [sum(X[j][i] for j in range(2)) / len(X) for i in range(3)]
    m2 = [sum(Y[j][i] for j in range(4)) / len(Y) for i in range(3)]
    print(m1, m2)


if __name__ == "__main__":
    main()
