n, q = map(int, input().split())
s = input()
cum = 0
for _ in range(q):
    qtype, x = map(int, input().split())

    if qtype == 1:
        cum += x % n
    else:
        x -= 1
        x = (x - cum) % n
        print(s[x])
