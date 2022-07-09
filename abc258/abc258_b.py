n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, list(input()))))

ans = []

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
for i in range(n):
    for j in range(n):
        for dir in dirs:
            tmp = ""
            for k in range(n):
                x, y = dir
                x, y = k * x, k * y
                i_ = (i + x) % n
                j_ = (j + y) % n
                tmp = tmp + str(a[i_][j_])
            ans.append(tmp)

print(max(ans))