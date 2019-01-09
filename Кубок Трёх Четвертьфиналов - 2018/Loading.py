try:
    import sys
    x = sys.stdin.readline().strip()
    if x.isdigit():
        n = int(x)
        summ = sum(list([int(x) if x.isdigit() else 0 for x in sys.stdin.readline().strip().split(' ')]))
        print(summ / n)
    else:
        print(0)
except Exception:
    print(0)
