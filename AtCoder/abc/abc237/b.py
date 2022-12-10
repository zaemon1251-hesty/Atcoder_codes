import numpy as np
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
A = np.array(A).T
B = A.tolist()
for b in B:
    print(*b)
