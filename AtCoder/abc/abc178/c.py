MOD = 10**9 + 7
N = int(input())
print((pow(10, N, MOD) - (pow(9, N, MOD)*2 - pow(8, N, MOD))) % MOD)
