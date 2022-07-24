n = int(input())
a = []
for i in range(n):
    a.append(list(input()))

for i in range(n):
    for j in range(n):
        if (
            a[i][j] == "-"
            or (a[i][j] == "D" and a[j][i] == "D")
            or (a[i][j] == "W" and a[j][i] == "L")
            or (a[i][j] == "L" and a[j][i] == "W")
        ):
            pass
        else:
            print("incorrect")
            exit()

print("correct")
