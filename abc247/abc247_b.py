from collections import Counter
n = int(input())

s = []
t = []
full = []
for i in range(n):
    si, ti = input().split()
    s.append(si)
    t.append(ti)
    fname = si + " " + ti
    if fname in full:
        print("No")
        exit()
    full.append(si + " " + ti)

s_set = set(s)
t_set = set(t)

cs = Counter(s)
ct = Counter(t)


for i in range(n):
    flag1 = False
    flag2 = False

    #name
    for j in range(n):
        if i==j:
            pass
        else:
            if (s[i]==s[j]) or (s[i]==t[j]):
                flag1 = True

    for j in range(n):
        if i==j:
            pass
        else:
            if (t[i]==s[j] or (t[i]==t[j])):
                flag2 = True
    
    if flag1 and flag2:
        print('No')
        exit()

print('Yes')