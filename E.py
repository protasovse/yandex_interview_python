import sys
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

l1 = list(s1)
l1.sort()
l2 = list(s2)
l2.sort()

print(1 if l1 == l2 else 0)
