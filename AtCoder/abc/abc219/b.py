def main():
    S = [input(), input(), input()]
    T = list(input())
    mapping = {str(i): s for i, s in zip(range(1, 4), S)}
    print("".join(map(lambda t: mapping[t], T)))


if __name__ == "__main__":
    main()
