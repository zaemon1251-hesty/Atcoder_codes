#ABC 190 E Magical Ornament
from collections import deque

inf=pow(10,9)
n,m=map(int,input().split())
G=[[] for _ in range(n)]

for i in range(m):
    s,e=map(int,input().split())
    G[s-1].append(e-1)
    G[e-1].append(s-1)

k=int(input())
row=list(map(lambda x:int(x)-1, input().split()))

#ciどうしの距離
dist=[[inf]*k for _ in range(k)]
#rowの各頂点に0~k-1を割り当てる
dic={row[i]:i for i in range(k)}

#k回のbfsにより頂点同士の最短距離を求める
for v in row:
  short=[inf]*n
  short[v]=0
  todo=deque([v])

  while todo:
      dd=todo.popleft()
      for to in G[dd]:
          if short[to] == inf:
            short[to]=short[dd]+1
            todo.append(to)
      
  for j in row:
    dist[dic[v]][dic[j]]=short[j]
    dist[dic[j]][dic[v]]=short[j]

# dp[s][i]は頂点集合sを全て通って頂点iで終わる道のうち最小となる辺の数
dp=[[inf]*(k) for _ in range(2**k)]

#bitDPの部分,k!の問題を(2^k)(k^2)で解ける
for s in range(1,2**k):
  for i in range(k):
    if s==(1<<i):dp[s][i]=1
    elif (s>>i)&1:
      dp[s][i]=min([dp[s^(1<<i)][j] + dist[i][j] for j in range(k)])
ans=min(dp[-1])
if ans==inf:
  ans=-1
print(ans)