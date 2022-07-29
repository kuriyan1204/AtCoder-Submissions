from collections import Counter, defaultdict
import string

# N, Aを標準入力から受け取る
n, a = map(int, input().split())

# 標準入力から受け取った文字列を保存する配列
s = []

# 標準入力から文字列をn個受け取る
for i in range(n):
    #s.append(defaultdict(int, Counter(input())))
    s.append(Counter(input()))

ans = 0
# Iterate over bit
for i in range(2 ** n):
    tmp = defaultdict(int)
    # if jth flag is true
    for j in range(n):
        if (i >> j) & 1:
            for c in list(string.ascii_lowercase):
                tmp[c] += s[j][c]
    tmp_set = set()
    for c in list(string.ascii_lowercase):
        if tmp[c] == a:
            tmp_set.add(c)
    ans = max(len(tmp_set), ans)
print(ans)