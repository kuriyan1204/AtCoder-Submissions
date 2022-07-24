from collections import defaultdict

n = int(input())
d = defaultdict(int)

ss = [input() for _ in range(n)]

for s in ss:
    if not d[s] == 0:
        print(f"{s}({d[s]})")
    else:
        print(s)

    d[s] += 1
