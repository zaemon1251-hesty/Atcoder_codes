<<<<<<< HEAD
from string import ascii_lowercase


def main():
    P = list(map(int, input().split()))
    alpha = ascii_lowercase
    print("".join(map(lambda x: alpha[x - 1], P)))


if __name__ == '__main__':
    main()
=======
from collections import defaultdict
N = int(input())
S = defaultdict(set)
for i in range(N):
    x, y = map(int, input().split())
    S[x].add(y)
X = S.keys()
ans = 0
for x1 in X:
    for x2 in X:
        if x1 == x2:
            continue
        tmp = len(S[x1] & S[x2])
        ans += tmp*(tmp - 1)//2
print(ans//2)
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
