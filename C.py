"""
Дан упорядоченный по неубыванию массив целых 32-разрядных чисел.
Требуется удалить из него все повторения.
Желательно получить решение, которое не считывает входной файл целиком в память, т.е.,
использует лишь константный объем памяти в процессе работы.
"""
import sys

count = sys.stdin.readline().strip()

ch = -1
res = []
for i in range(int(count)):
    el = sys.stdin.readline().strip()
    if el != ch:
        res.append(el)
    ch = el

for i in res:
    print(i)

