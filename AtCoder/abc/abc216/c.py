<<<<<<< HEAD
N = int(input())
ans = ""
while N > 0:
    if N % 2 == 0:
        N //= 2
        ans += "B"
    else:
        N -= 1
        ans += "A"
print("".join(list(ans)[::-1]))
=======
N, K = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
A.append(0)
ans = 0
for i in range(N):
    if K == 0:
        break
    s = A[i] - A[i+1]
    rest = 0
    if (i + 1)*s > K:
        s = K//(i + 1)
        rest = K % (i + 1)
    adds = (s*A[i] - s*(s-1)//2) * (i + 1)
    if rest != 0:
        adds += (A[i] - s) * rest
    ans += adds
    K -= s * (i + 1) + rest
print(ans)
e()
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
