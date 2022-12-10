import string


ch = string.ascii_lowercase
N = int(input())
ans = []
# 長さを決定する
times = 1
while N > pow(26, times):
    N -= pow(26, times)
    times += 1
# 答えを求める
N -= 1
while N:
    ans.append(ch[N % 26])
    N //= 26
if len(ans) != times:
    ans.append(ch[0]*(times - len(ans)))
print(*ans[::-1], sep="")
