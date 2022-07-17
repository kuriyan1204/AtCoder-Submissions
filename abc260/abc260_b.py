n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

acc = set()

a_i = sorted([(i, a[i]) for i in range(n)], key=lambda x: x[1], reverse=True)
b_i = sorted([(i, b[i]) for i in range(n)], key=lambda x: x[1], reverse=True)
c_i = sorted([(i, a[i] + b[i]) for i in range(n)], key=lambda x: x[1], reverse=True)

cnt = 0
for i in range(n):
    if cnt == x:
        break

    if not a_i[i][0] in acc:
        cnt += 1
        acc.add(a_i[i][0])


cnt = 0
for i in range(n):
    if cnt == y:
        break

    if not b_i[i][0] in acc:
        cnt += 1
        acc.add(b_i[i][0])

cnt = 0
for i in range(n):
    if cnt == z:
        break

    if not c_i[i][0] in acc:
        cnt += 1
        acc.add(c_i[i][0])

acc = sorted(list(acc))
for i in acc:
    print(i + 1)
