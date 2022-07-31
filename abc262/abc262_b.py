n, m = map(int, input().split())
g = [[-1] * n for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a][b] = 1
    g[b][a] = 1

cnt = 0
for a in range(n - 2):
    for b in range(a + 1, n - 1):
        for c in range(b + 1, n):
            if g[a][b] == 1 and g[b][c] == 1 and g[a][c] == 1:
                cnt += 1

print(cnt)