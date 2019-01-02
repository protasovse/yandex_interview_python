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
    li = [int(l) if l.isdigit() else 0 for j, l in enumerate(s.split(' ')) if j <= num]
    del s
    for l in li[1:]:
        t[l] += 1

res = []
for i in range(101):
    res += [i] * t[i]

for r in res:
    print(r, end=' ')
