import sys

int_list, counter, pointer = [], [], []
n = int(sys.stdin.readline().strip())
for i in range(int(n)):
    s = input()
    li = s.split(' ')
    num = int(li[0])
    counter.append(num+1)
    pointer.append(1)
    int_list.append(list([int(l) for l in li[0:num + 1]]))

while counter != pointer:
    mi, j, i = 100, 0, 0
    for l in int_list:
        if pointer[i] < counter[i]:
            if l[pointer[i]] <= mi:
                mi = l[pointer[i]]
                j = i
        i += 1
    pointer[j] += 1
    sys.stdout.write('%d ' % (mi, ))
print('\n')
