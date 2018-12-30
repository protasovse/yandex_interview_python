import sys

n = int(sys.stdin.readline().strip())
int_list = []
for i in range(n):
    input = sys.stdin.readline().strip()
    data = list(map(int, input.split()))
    input = None
    n = data[0]
    a = data[1:n+1]
    int_list.extend(a)
    data = None

int_list.sort()

for li in int_list:
    sys.stdout.write(str(li) + ' ')
sys.stdout.write('\n')

