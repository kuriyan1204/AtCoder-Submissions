from itertools import accumulate

q = int(input())
idx = 0
mem = []
for i in range(q):
    que = list(input().split())
    if que[0] == "1":
        x = int(que[1])
        c = int(que[2])
        mem.append([x, c])
    else:
        c = int(que[1])
        sum = 0
        while True:
            if mem[idx][1] - c == 0:
                sum += mem[idx][1] * mem[idx][0]
                idx += 1
                print(sum)
                break
            elif mem[idx][1] - c > 0:
                sum += mem[idx][0] * c
                mem[idx][1] = mem[idx][1] - c
                print(sum)
                break
            else:
                sum += mem[idx][1] * mem[idx][0]
                c -= mem[idx][1]
                idx += 1