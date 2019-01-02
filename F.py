import sys

int_list = []
t = [0] * 101
n = int(sys.stdin.readline().strip())
for i in range(int(n)):
    s = sys.stdin.readline().strip()
    try:
        num = int(s[:s.find(' ')])
    except ValueError:
        continue
    for index, value in enumerate(s.split(' ')):
        if index == 0:
            continue
        elif index == num + 1:
            break
        try:
            t[int(value)] += 1
        except ValueError:
            pass

res = []
for i in range(101):
    res += [i] * t[i]

for r in res:
    print(r, end=' ')
