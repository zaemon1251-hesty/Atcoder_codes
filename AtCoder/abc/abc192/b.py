S = input()
for i in range(len(S)):
    if i % 2 == 0 and S[i].lower() == S[i]:
        continue
    if i % 2 == 1 and S[i].upper() == S[i]:
        continue
    print("No")
    exit()
print("Yes")
