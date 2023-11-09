from collections import defaultdict


def main():
    N = int(input())
    S = list(map(int, list(input())))
    W = list(map(int, input().split()))

    Train = sorted(list(zip(W, S)), key=lambda x: x[0])
    # Train.append((1 << 60, False))
    G = defaultdict(list)
    for w, s in Train:
        G[w].append(s)
    childs = 0
    unkn = N
    true_ad = S.count(1)
    ans = true_ad
    tried = set()
    for w, s in Train:
        if w in tried:
            continue
        ads = sum(G[w])

        childs += len(G[w]) - ads
        unkn -= len(G[w])
        true_ad -= ads

        ans = max(ans, childs + true_ad)
        tried.add(w)

    ans = max(ans, S.count(0))
    print(ans)


if __name__ == "__main__":
    main()
