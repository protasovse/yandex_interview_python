file = open('./input.txt', 'r').readline()
n = [int(x) for x in file.strip().split(' ')]
file2 = open('./output.txt', 'w')
file2.write(f'{n[0]+n[1]}')
file2.close()
