<<<<<<< HEAD
from collections import Counter


def main():
    n = int(input())
    A = Counter(map(int, input().split()))
    B = list(map(int, input().split()))
    C = Counter(map(lambda x: int(x) - 1, input().split()))
    ans = 0
    for k, v in C.items():
        val = B[k]
        ans += v * A[val]
    print(ans)


if __name__ == "__main__":
    main()
=======
n = int(input())
from collections import Counter
from bisect import bisect_left, bisect_right
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = Counter(list(map(lambda x:int(x) - 1, input().split())))
ans = 0
for k,v in C.items():
    val = B[k]
    ans += v * (bisect_right(A, val) - bisect_left(A, val))
print(ans)
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
