s = list(input())
from collections import Counter

s = sorted(list(Counter(s).items()), key=lambda x: x[1])

if s[0][-1] == 1:
    print(s[0][0])
else:
    print(-1)