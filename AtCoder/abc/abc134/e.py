from bisect import bisect_right

N = int(input())
A = [int(input()) for _ in range(N)]

anti_chain = []
for a in A:
    a *= -1
    idx = bisect_right(anti_chain, a)
    if idx == len(anti_chain):
        anti_chain.append(a)
    else:
        anti_chain[idx] = a

print(len(anti_chain))
