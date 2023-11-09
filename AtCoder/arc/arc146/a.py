def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(key=lambda x: (x, str(x)))
    print("".join(map(str, sorted([A[-1], A[-2], A[-3]], key=lambda x: str(x), reverse=True))))


if __name__ == "__main__":
    main()
