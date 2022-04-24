from collections import defaultdict, Counter


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


if __name__ == "__main__":
    ans = 0
    n = int(input())
    a = list(map(int, input().split()))
    maps = defaultdict(int, Counter(a))
    for ai in a:
        divs = make_divisors(ai)
        for div in divs:
            div_ = ai // div
            if ai == div_ * div:
                ans += maps[div] * maps[div_]
    print(ans)
