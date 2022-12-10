
def main():
    from string import ascii_lowercase

    SIZE_OF_CHRS = 26
    cv = {c: i for i, c in enumerate(ascii_lowercase)}

    n = int(input())
    *s, = input()

    a = [[] for _ in range(SIZE_OF_CHRS)]
    for i, c in enumerate(s):
        a[cv[c]].append(i)

    b = []
    for i in reversed(range(SIZE_OF_CHRS)):
        b += a[i]  # [z昇順]+[y昇順]+...+[a昇順]

    k = n
    for i, c in enumerate(s):
        while b and s[b[-1]] < c:
            j = b.pop()
            if i < j < k:
                s[i], s[j] = s[j], s[i]
                k = j
                break

    print(*s, sep='')


if __name__ == "__main__":
    main()
