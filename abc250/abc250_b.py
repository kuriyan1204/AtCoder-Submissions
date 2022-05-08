n,a,b = map(int,input().split())

base1 = ''
base2 = ''
for i in range(n):
    if i %2 == 0:
        base1 += '.'*b
        base2 += '#'*b
    else:
        base1 += '#'*b
        base2 += '.'*b

for i in range(n):
    if i%2 ==0:
        for j in range(a):
            print(base1)
    else:
        for j in range(a):
            print(base2)