a,b,c = map(int, input().split())
if pow(a,b) > pow(a,c):
    print('>')
elif pow(a,b) == pow(a,c):
    print('=')
else:
    print('<')
