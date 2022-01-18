n = int(input())
R = list(map(int, input().split()))
C = list(map(int, input().split()))
q = int(input())
rc = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(q)]
ans = []
for r, c in rc:
    t1 = min(R[r], C[c])
    t2 = max(R[r], C[c])
    if t1 + t2 > n:
        ans.append("#")
    elif n % 2 != 0 and t1 == t2 == (n + 1)//2:
        ans.append("#")
    else:
        ans.append(".")
print(*ans, sep="")
