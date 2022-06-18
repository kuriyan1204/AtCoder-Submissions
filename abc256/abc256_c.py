h1, h2, h3, w1, w2, w3 = map(int, input().split())
cnt = 0
for a1 in range(1, 31):
    for a2 in range(1, 31):
        for a4 in range(1, 31):
            for a5 in range(1, 31):
                a3 = h1 - (a1 + a2)
                a6 = h2 - (a4 + a5)
                a7 = w1 - (a1 + a4)
                a8 = w2 - (a2 + a5)
                a9 = w3 - (a3 + a6)
                if (a3 < 1) or (a6 < 1) or (a7 < 1) or (a8 < 1) or (a9 < 1):
                    pass
                else:
                    if (
                        (a1 + a2 + a3 == h1)
                        and (a4 + a5 + a6 == h2)
                        and (a7 + a8 + a9 == h3)
                        and (a1 + a4 + a7 == w1)
                        and ((a2 + a5 + a8 == w2))
                        and (a3 + a6 + a9 == w3)
                    ):
                        cnt += 1

print(cnt)