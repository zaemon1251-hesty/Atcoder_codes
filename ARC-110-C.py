#ちょうど一回の隣接swappingだけでソート出きるか判定
n = int(input())
l = list(map(int,input().split()))
d = {l[i]:i+1 for i in range(n)}
r=[]
xf=0
for i in range(1,n+1):
    #print('now',i)
    for j in range(d[i]-1,i-1,-1):
        r.append(j)
        d[l[j-1]]+=1
        #print(j)
        f=1
        if len(r)>n-1:
            #print(r)
            print(-1)
            xf=1
            break
    if xf==1:
        break
if xf!=1:
    if len(set(r))==len(r)==n-1:
        for i in r:
            print(i)
    else:
        print(-1)