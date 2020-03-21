import functools


# 1.0 - write a oneliner function that attaches a symbol to every element of an iterable
# and prints all elements as a single string
def combine_coins(symbol, gen):
    return ", ".join(map(lambda x: symbol + str(x), gen))


print(combine_coins('$', range(5)))


# 1.1.2 - write a oneliner function that doubles every character in a string
def double_letter(my_str):
    return ''.join((map(lambda x: x * 2, my_str)))


print(double_letter("python"))


# 1.1.3 - write a oneliner function that receives a number and returns
# all numbers that can be divided by four up to that number
def four_dividers(number):
    return list(filter(lambda x: x % 4 == 0, range(1, number + 1)))


print(four_dividers(9))
print(four_dividers(3))


# 1.1.4 - write a oneliner function that receives a number and returns its sum of digits
def sum_of_digits(number):
    return functools.reduce(lambda x, y: x + y, map(lambda x: int(x), str(number)), 0)


print(sum_of_digits(104))
