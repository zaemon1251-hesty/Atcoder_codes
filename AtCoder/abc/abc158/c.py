A, B = map(int, input().split())
for p in range(20000):
    if int(p * 0.08) == A and int(p * 0.1) == B:
        print(p)
        exit()
print(-1)
