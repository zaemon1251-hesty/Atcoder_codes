A, B = map(int, input().split())
while A and B:
    a, A = A % 10, A // 10
    b, B = B % 10, B // 10
    if a + b >= 10:
        print("Hard")
        exit()
print("Easy")
