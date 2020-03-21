import functools

# 1.5.1 - write a function that prints the longest name in the file nextpy1.5names.txt
with open('nextpy1.5names.txt', 'r') as f:
    print(functools.reduce(lambda x, y: x if len(x) > len(y)
                           else y, f.read().splitlines()))


# 1.5.2 - write a function that prints the sum of length of names in nextpy1.5names.txt
with open('nextpy1.5names.txt', 'r') as f:
    print(functools.reduce(lambda x, y: x + len(y) if type(x) == int else len(x) + len(y),
                           f.read().splitlines()))


# 1.5.3 - write a function that prints all of the shortest names in nextpy1.5names.txt
with open('nextpy1.5names.txt', 'r') as f:
    lines = sorted(f.read().splitlines(), key=len)
    print('\n'.join(filter(lambda x: len(x) == len(lines[0]), lines)))


# 1.5.4 - write a function that writes the length of every name in nextpy1.5names.txt into nextpy1.5name_length.txt
with open('nextpy1.5names.txt', 'r') as f:
    with open('nextpy1.5name_length.txt', 'w') as fw:
        fw.writelines([str(len(line.strip())) + '\n' for line in f.readlines()])


# 1.5.5 - write a function that takes an int as input and prints all names in nextpy1.5names.txt of that length
with open('nextpy1.5names.txt', 'r') as f:
    length = int(input("enter name length: "))
    [print(line) for line in filter(lambda x: len(x) == length,
                                    [l.strip() for l in f.readlines()])]
