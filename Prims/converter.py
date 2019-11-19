f = open('routes_mod.txt', 'r')
fout = open('proutes.txt', 'w')
for line in f:
    line = line.strip().split(' ')
    fout.write(', '.join(line) + '\n')
f.close()
fout.close()
