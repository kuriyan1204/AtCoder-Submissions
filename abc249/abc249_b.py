s = input()

big = False
small = False
set_ = set()
for c in s:
    if c.islower():
        small = True
    else:
        big = True

    if c in set_:
        print("No")
        exit()
    set_.add(c)

if big and small:
    print('Yes')
else:
    print('No')