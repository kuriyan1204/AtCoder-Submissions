n, m, x, t, d = map(int, input().split())
ans = {}
cur = t - d * x
ans[0] = cur
for i in range(1, n + 1):
    if i < (x+1):
        cur += d
        ans[i] = cur
    else:
        ans[i] = cur

print(ans[m])