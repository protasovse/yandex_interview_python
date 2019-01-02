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
    li = []
    for j, l in enumerate(s.split(' ')):
        if l.isdigit():
            li.append(int(l))
        if j == num:
            break

    for l in li[1:]:
        t[int(l)] += 1
    del s

res = []
for i in range(101):
    res += [i] * t[i]

for r in res:
    print(r, end=' ')
