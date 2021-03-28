import itertools
alphabets = ['1', 'x', 'y', 'z', 'Z']
f = open("dict.txt", "w")
for passlen in [5]:
    combinations = itertools.product(alphabets, repeat = passlen)
    for combination in combinations:
        f.write(''.join(combination)+"\n")