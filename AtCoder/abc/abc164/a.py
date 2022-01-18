S = list(input())[::-1]
mod = [0]*2019
mod[0] += 1
r = 0
ten = 1
for i in range(len(S)):
    r += int(S[i])*ten
    r %= 2019
    mod[r] += 1
    ten *= 10
    ten %= 2019
ans = 0
for item in mod:
    ans += item * (item - 1) // 2
print(ans)
_name__ == "__main__":
maind()