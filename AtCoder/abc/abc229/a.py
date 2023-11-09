s1 = list(input())
s2 = list(input())
s1 = [i for i in range(len(s1)) if s1[i] == "#"]
s2 = [i for i in range(len(s2)) if s2[i] == "#"]
if len(s1) == len(s2) == 1:
    if s1[0] != s2[0]:
        print("No")
        exit()
print("Yes")
