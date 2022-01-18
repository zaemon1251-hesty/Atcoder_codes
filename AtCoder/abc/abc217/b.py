a, b, c = map(str, input().split())
g = [a, b, c]
an = ["abc", "agc", "arc", "ahc"]
for ans in an:
    if not ans in g:
        print(ans)
        exit()
