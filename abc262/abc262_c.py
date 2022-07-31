

cnt = 0
n = int(input())
a = list(map(int, input().split()))
cn = [i for i in range(n)]
ans = []
ans_ = []
for i in range(n):
    x = a[i] - 1
    if x == i:
        ans.append(i)
    else:
        j = x
        if (
            min(a[i], a[j]) == min(i + 1, j + 1)
            and max(a[i], a[j]) == max(i + 1, j + 1)
            and i < j
        ):
            cnt += 1
            # ans_.append((i, j))

if len(ans) <= 1:
    print(cnt)
else:
    n = len(ans)
    print(cnt + (n) * (n - 1) // 2)

# print(cnt)
# print(ans)
# print(ans_)

# ans_ = []
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if max(a[i], a[j]) == j + 1 and min(a[i], a[j]) == i + 1:
#             ans_.append((i, j))
# print(ans_)