H, W, K = map(int, input().split())
C = [list(input())
     for _ in range(H)]
ans = 0

for i in range(1 << H):
    use_h = []
    for h in range(H):
        if i >> h & 1:
            use_h.append(h)
    for j in range(1 << W):
        use_w = []
        for w in range(W):
            if j >> w & 1:
                use_w.append(w)
        cnt = 0
        for h in use_h:
            for w in use_w:
                cnt += 1 if C[h][w] == "#" else 0
        if cnt == K:
            ans += 1

print(ans)
