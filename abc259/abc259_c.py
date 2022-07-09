s = input()
t = input()

s_char = []
s_len = []
t_char = []
t_len = []

prev = s[0]
cnt = 1
for i in range(1, len(s)):
    if s[i] != prev:
        s_char.append(s[i - 1])
        s_len.append(cnt)
        cnt = 0

    prev = s[i]
    cnt += 1
if s[len(s) - 1] != s[len(s) - 2]:
    s_char.append(s[len(s) - 1])
    s_len.append(1)
else:
    s_char.append(s[len(s) - 1])
    s_len.append(cnt)

prev = t[0]
cnt = 1
for j in range(1, len(t)):

    if t[j] != prev:
        t_char.append(t[j - 1])
        t_len.append(cnt)
        cnt = 0

    prev = t[j]
    cnt += 1
if t[len(t) - 1] != t[len(t) - 2]:
    t_char.append(t[len(t) - 1])
    t_len.append(1)
else:
    t_char.append(t[len(t) - 1])
    t_len.append(cnt)

if len(s_char) != len(t_char):
    print("No")
else:
    for i in range(len(s_char)):
        if not (s_char[i] == t_char[i]):
            print("No")
            exit()
        if s_len[i] == t_len[i]:
            pass
        else:
            if not (s_len[i] <= t_len[i] and s_len[i] >= 2):
                print("No")
                exit()

    print("Yes")