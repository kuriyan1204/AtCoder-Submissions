import bisect
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
q = int(input())

d = defaultdict(list)
for i, ai in enumerate(a):
    d[ai].append(i)

for _ in range(q):
    l, r, x = map(int, input().split())
    l_ = bisect.bisect_left(d[x], l - 1)
    r_ = bisect.bisect_left(d[x], r)
    print(r_ - l_)
