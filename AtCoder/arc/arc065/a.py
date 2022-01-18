S = list(input())
buff = []
comp = {"eam": "dr", "mer": "drea", "ase": "er", "ser": "era"}
flg = True
while S:
    buff.append(S.pop())
    if len(buff) == 3:
        op = "".join(buff[::-1])
        for co in comp.keys():
            if op == co:
                break
        else:
            print("NO")
            exit()
        buff = []
        for _ in range(len(comp[op])):
            buff.append(S.pop())
        if "".join(buff[::-1]) != comp[op]:
            flg = False
        buff = []
if buff or not flg:
    print("NO")
else:
    print("YES")
c()
