n = int(input())

s1 = ["1"]

y = 2


if n == 1:
    print(1)
    exit()

for i in range(n - 1):
    s1 = s1 + [str(y)] + s1
    y += 1

print(" ".join(s1))
