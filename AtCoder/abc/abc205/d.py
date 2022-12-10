from bisect import bisect, bisect_left
N, Q = map(int, input().split())
A = list(map(int, input().split()))
rest = [0]
for i in range(N):
    if i == 0:
        a = 0
        b = A[i] - 1
    else:
        a = rest[-1]
        b = A[i] - A[i - 1] - 1
    rest.append(a + b)
    if i == N - 1:
        rest.append(10**18)
A = [0] + A
for i in range(Q):
    K = int(input())
    idx = bisect_left(rest, K)
    K -= rest[idx - 1]
    ans = A[idx - 1] + K
    print(ans)
    #print(f"K:{K}, idx:{idx}, ans:{ans}")
_name__ =="__main__":
mori = 20
#maina()
#mainb()
#mainc()
maind()
#maine()