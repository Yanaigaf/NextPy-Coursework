'''
Define function Parse_ranges which receives a string of int ranges to parse. example "1-2,4-4,8-10"
Use generator expressions
'''


def parse_ranges(string2parse):
    one_range = (one.split('-') for one in string2parse.split(','))
    for i, j in one_range:
        for x in range(int(i), int(j) + 1):
            yield x


def main():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))


if __name__ == "__main__":
    main()
