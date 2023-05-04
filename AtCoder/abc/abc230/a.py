<<<<<<< HEAD
def main():
    N = int(input())
    if N >= 42:
        N += 1
    print("AGC%03d" % N)


if __name__ == '__main__':
    main()
=======
from math import ceil, floor
N = int(input())
ans = 0
for i in range(1, 10**6):
    if i > N:
        print(ans)
        exit()
    ans += i * (floor(N/i) - ceil(N/(i+1)) + 1 - int(N % (i+1) == 0))
for i in range(1, floor(N/10**6)+1):
    ans += floor(N/i)
print(ans)
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
