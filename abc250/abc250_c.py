n,q = map(int,input().split())
#value,index
val_idx = {i:i for i in range(1,n+1)}
#idx,val
idx_val = {i:i for i in range(1,n+1)}

for _ in range(q):
    x = int(input())
    x_idx = val_idx[x]
    if x_idx+1 == n+1:
        to_idx = x_idx -1
    else:
        to_idx = x_idx +1
    to = idx_val[to_idx]

    #swap
    val_idx[x] = to_idx
    val_idx[to] = x_idx

    idx_val[x_idx] = to
    idx_val[to_idx] = x

print(' '.join([str(idx_val[i]) for i in range(1,n+1)]))
