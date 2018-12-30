import collections
import sys
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
l1 = list(s1)
l2 = list(s2)

c1 = collections.Counter()
c2 = collections.Counter()

for word in l1:
    c1[word] += 1

for word in l2:
    c2[word] += 1

print(1 if c1 == c2 else 0)
