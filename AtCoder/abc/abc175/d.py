import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
if __name__ == "__main__":
    N, K = map(int, input().split())
    P = list(map(lambda x: int(x)-1, input().split()))
    C = list(map(int, input().split()))
    ans = -float("inf")
    for i in range(N):
        sm = 0
        j = i
        ls = []
        while True:
            j = P[j]
            sm += C[j]
            ls.append(sm)
            if j == i:
                break
        for j in range(min(K, len(ls))):
            score = ls[j]
            k = K-j-1
            if k >= len(ls) and sm > 0:
                score += (k // len(ls)) * sm
            ans = max(ans, score)
    print(ans)
