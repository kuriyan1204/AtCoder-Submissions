n = int(input())
s = []
t = []
used = set({})
origs = []
for i in range(n):
    si, ti = input().split()
    ti = int(ti)
    s.append(si)
    t.append(ti)
    if not si in used:
        used.add(si)
        origs.append(i)

ans = [[i, t[i]] for i in origs]
ans = sorted(ans, key=lambda x: -x[-1])

print(ans[0][0]+1)