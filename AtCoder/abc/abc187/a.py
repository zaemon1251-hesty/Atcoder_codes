def main():
    A, B = map(str, input().split())

    def p(w):
        w = map(int, list(w))
        return sum(w)

    print(max(p(A), p(B)))


if __name__ == "__main__":
    main()
