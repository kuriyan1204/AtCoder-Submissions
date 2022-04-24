a, b, c, d, e, f, x = map(int, input().split())

tak = x
aok = x
cnt1 = 0
cnt2 = 0
while tak >= 0:

    if tak - a >= 0:
        cnt1 += a
        tak = tak - a
    else:
        cnt1 += tak
        break

    if tak - c >= 0:
        tak = tak - c
    else:
        break

while aok >= 0:

    if aok - d >= 0:
        cnt2 += d
        aok = aok - d
    else:
        cnt2 += aok
        break

    if aok - f >= 0:
        aok = aok - f
    else:
        break

if cnt1 * b > cnt2 * e:
    print("Takahashi")
elif cnt1 * b == cnt2 * e:
    print("Draw")
else:
    print("Aoki")
