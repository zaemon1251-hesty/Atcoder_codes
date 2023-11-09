from itertools import permutations


def main():
    S = input().split()
    T = input().split()
    a = set()
    cnt = 0
    todo = [tuple(S)]
    flg = True
    while flg:
        tmp = []
        for s in todo:
            s = todo.pop()
            if s in a:
                continue
            if all(s[i] == T[i] for i in range(3)):
                flg = False
                break
            tmp.append((s[1], s[0], s[2]))
            tmp.append((s[0], s[2], s[1]))
            tmp.append((s[2], s[1], s[0]))
            a.add(s)
        todo = tmp
        cnt += 1
    cnt -= 1
    print("Yes" if cnt % 2 == 0 else "No")


if __name__ == "__main__":
    main()
