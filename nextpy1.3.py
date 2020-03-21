import functools


# 1.3.1 - write a oneliner function that receives 2 lists and returns
# a list which consists of only elements which appeared in both lists, with no duplicates
def intersection(list_1: list, list_2):
    return list(set(list_1) & set(list_2))


print(intersection([5, 5, 6, 6], [1, 7, 5, 6]))


# 1.3.3 - write a oneliner function that receives a string and returns true if it consists only of the letters
# 'a' and 'h' and false otherwise
def is_funny(string):
    return functools.reduce(lambda x, y: x and y, [(x == 'h' or x == 'a') for x in string])


print(is_funny('ahahahahah'))
print(is_funny('nice dog'))


# 1.3.4 - write a oneliner function that receives the provided hashed string and cracks it by adding
# 2 to all ascii-representable alphanumerical characters
def crack(password):
    return ''.join(chr(ord(s) + 2) if s.isalpha() else s for s in password)


print(crack(password="sljmai ugrf rfc ambc: lglc dmsp mlc rum"))
