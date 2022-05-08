h,w = map(int,input().split())
r,c = map(int,input().split())

cnt = 0

for x in [(1,0),(-1,0),(0,1),(0,-1)]:
    i,j = x
    if 1<=r+i<=h and 1<=c+j<=w:
      cnt+=1

print(cnt)