from collections import Counter, defaultdict
import string

n, k = map(int, input().split())

s = []

for i in range(n):
    s.append(defaultdict(int, Counter(input())))

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
        if tmp[c] == k:
            tmp_set.add(c)
    ans = max(len(tmp_set), ans)
print(ans)