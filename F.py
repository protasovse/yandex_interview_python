import sys

int_list = []
n = int(sys.stdin.readline().strip())
for i in range(int(n)):
    s = sys.stdin.readline().strip()
    li = s.split(' ')
    num = int(li[0])
    int_list.extend([int(l) for l in li[1:num + 1]])
for i in sorted(int_list):
    sys.stdout.write('%d ' % (i,))