# Removes parens and commas from routes file

with open('routes.txt', 'r') as f:
    with open('routes_mod.txt', 'w') as fout:
        txt = [line.strip()[1:-1].split(', ') for line in f]
        for line in txt:
            fout.write(' '.join(line))
            fout.write('\n')
