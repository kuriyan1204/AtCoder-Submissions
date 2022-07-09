k = int(input())

h = k // 60
m = k % 60

if h == 1:
    if 0 <= m <= 9:
        print(f"22:0{m}")
    else:
        print(f"22:{m}")
else:
    if 0 <= m <= 9:
        print(f"21:0{m}")
    else:
        print(f"21:{m}")
