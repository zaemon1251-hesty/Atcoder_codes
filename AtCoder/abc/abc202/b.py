s = list(input())
ans = ''
for i in s:
    if i == "9":
        ans = '6' + ans
    elif i == "6":
        ans = "9" + ans
    else:
        ans = i + ans
print(ans)
