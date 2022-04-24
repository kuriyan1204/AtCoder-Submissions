t = set({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
s = set(map(int, list(input())))
z = list(t - s)
print(z[0])
