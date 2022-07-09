n, x = map(int, input().split())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

cums = []
cum = 0
ans = []
for i in range(n):
    cum += a[i] + b[i]
    # cum.append((a[i], i + 1))

    if i + 1 >= x:
        ans.append(cum)
    else:
        rem = x - (i + 1)
        ans.append(cum + b[i] * rem)

print(min(ans))
