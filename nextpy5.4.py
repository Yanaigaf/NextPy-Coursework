'''
5.4
1 - write a function check_id_valid that will check if an int is a valid ID number according to these rules:
    for a digit at an odd index - multiply the digit by 1. for a digit at an even index - multiply the digit by 2
    if the multiplication results in a double digit number - add up its digits
    add up all 9 numbers. if result % 10 == 0 the id is valid
2 - Implement class IDIterator with attributes:
    _id, represents an int ID number
    __iter__
    __next__, returns the next valid id number from _id until 999999999
    no generators allowed
3 - create an iterator of class IDIteato in main(). initialize id as 123456780 and print 10 valid ids
4 - write a generator function id_generator which generates 1 valid id each time
5 - generate 10 ids from id_generator(123456780) in main and print them
'''


class IDIterator:
    '''A class used to iterate over valid ID numbers
    :param initial_id: ID number to start iteration from, type int, default 100000000
    '''

    def __init__(self, initial_id=100000000):
        self._id = initial_id - 1

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self._id += 1
            try:
                if check_id_valid(self._id):
                    return self._id
            except ValueError:
                raise StopIteration


def id_generator(id_number=100000000):
    '''Generator function used to generate valid ID numbers
    :param id_number: ID number to start generating from, type int, default 100000000
    yields the next valid ID number
    '''
    while id_number <= 999999999:
        if check_id_valid(id_number):
            yield id_number
        id_number += 1


def check_id_valid(id_number):
    '''Checks if a number is a valid ID number
    :param id_number: ID number to check, type int
    :return: True if ID is valid, otherwise False, type bool
    '''
    if id_number < 100000000 or id_number >= 999999999:
        raise ValueError("Expected an ID number consisting of 9 digits")
    digits = split_to_digits(id_number)
    digits_times_index = [sum(split_to_digits((index % 2 + 1) * num))
                          for index, num in enumerate(digits)]
    if sum(digits_times_index) % 10 == 0:
        return True
    return False


def split_to_digits(num):
    '''splits an int to a list of its digits
    :param num: the number to split to digits, type int
    :return: a list consisting of the numbers' digits, type list
    '''
    if num < 10:
        return [num]
    return split_to_digits(num // 10) + [num % 10]


def main():
    id_from_class = iter(IDIterator(123456780))
    id_from_gen = id_generator(123456780)
    for i in range(10):
        print(f'id # {i + 1} from class iterator: {next(id_from_class)}')
    for i in range(10):
        print(f'id # {i + 1} from generator function: {next(id_from_gen)}')


if __name__ == "__main__":
    main()
