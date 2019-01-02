import sys

int_str = ''
n = int(sys.stdin.readline().strip())
for i in range(int(n)):
    s = sys.stdin.readline().strip() + ' '
    count = int(s[:s.find(' ')])
    p, j = 0, 0
    for j in range(s.__len__()):
        if s[j] == ' ':
            p += 1
        if p == count+1:
            break
    int_str += s[s.find(' '):j]
    del (s,)

for i in sorted(int_str.lstrip().split(' '), key=lambda x: int(x) if x.isdigit() else 0):
    print(i, end=" ")

# 5
# 5 2 26 64 88 96 96
# 4 8 20 65 86
# 7 1 4 16 42 58 61 69
# 1 84
# 0
