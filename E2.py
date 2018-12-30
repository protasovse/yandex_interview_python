import sys
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
l1 = list(s1)
l2 = list(s2)

while l1:
    li = l1.pop()
    if li in l2:
        l2.remove(li)
    else:
        print(0)
        sys.exit()
print(1 if not l2 else 0)
