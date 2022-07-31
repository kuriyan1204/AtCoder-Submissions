y = int(input())

years = [(2002 + 4 * i) for i in range(251)]
ans = 2002
for i in range(2000, 3001):
    if i in years:
        ans = i
    if ans >= y:
        print(ans)
        exit()
print(3002)