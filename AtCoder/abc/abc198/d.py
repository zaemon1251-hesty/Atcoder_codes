from itertools import permutations


def main():
    SS = [list(input()) for _ in range(3)]
    words = set()
    for s in SS:
        for w in s:
            words.add(w)
    words = list(words)
    if len(words) > 10:
        print("UNSOLVABLE")
        exit()
    for perm in permutations(range(10), len(words)):
        ch = {words[i]: str(r) for i, r in enumerate(perm)}
        if any(ch[s[0]] == "0" for s in SS):
            continue
        NN = [int("".join(map(lambda x: ch[x], s))) for s in SS]
        if NN[0] + NN[1] == NN[2]:
            print(*NN, sep="\n")
            exit()
    print("UNSOLVABLE")


if __name__ == "__main__":
    main()
