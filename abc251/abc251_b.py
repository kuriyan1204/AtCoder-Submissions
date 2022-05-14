n, w = map(int, input().split())
a = list(map(int, input().split()))

ans = set()

for i in range(len(a)):
    ans.add(a[i])

if len(a) >= 2:
    for i in range(len(a)-1):
        for j in range(i + 1, len(a)):
            if not i == j:
                ans.add(a[i] + a[j])
if len(a) >= 3:
    for i in range(len(a) - 2):
        for j in range(i + 1, len(a) - 1):
            for k in range(j + 1, len(a)):
                ans.add(a[i] + a[j] + a[k])

ans = list(ans)
ans = sorted(ans)

cnt = 0
for i in range(len(ans)):
    if ans[i] <= w:
        cnt += 1
print(cnt)