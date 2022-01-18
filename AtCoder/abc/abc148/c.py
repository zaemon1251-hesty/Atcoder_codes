n = int(input())
if n % 2 != 0:
    print(0)
    exit()
i = 10
devide = []
while n // i > 0:
    devide.append(n // i)
    i *= 5
print(sum(devide))
_name__ == "__main__":
maind()
