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
