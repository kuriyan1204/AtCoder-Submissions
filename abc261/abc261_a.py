l1, r1, l2, r2 = map(int, input().split())

red = set(range(l1, r1))
blue = set(range(l2, r2))

print(len(red.intersection(blue)))