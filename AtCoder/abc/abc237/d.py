from collections import deque


N = int(input())
*S, = input()


class Node:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.left = left
        self.right = right


now = Node(0)
for i in range(N):
    if S[i] == "L":
        if not now.left:
            now.left = Node(i + 1, right=now)
        else:
            p = now.left
            now.left = Node(i + 1, right=now, left=p)
            p.right = now.left
        now = now.left
    else:
        if not now.right:
            now.right = Node(i + 1, left=now)
        else:
            p = now.right
            now.right = Node(i + 1, left=now, right=p)
            p.left = now.right
        now = now.right
ans = deque([])
cr = now
while now:
    ans.appendleft(now.data)
    now = now.left
now = cr.right
while now:
    ans.append(now.data)
    now = now.right

print(*list(ans))
