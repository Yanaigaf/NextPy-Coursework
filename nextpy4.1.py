'''
4.1.2
Define a translate function with a dictionary of spanish word -→ english word. Implement the translation using a generator
'''


def translate(spanish_sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in',
             'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translation = ' '.join(words[word] for word in spanish_sentence.split())
    return translation


def main():
    print(translate("el gato esta en la casa"))


if __name__ == "__main__":
    main()


'''
4.1.3
Define a function that receives a number n as input and returns the first prime number *after* n. must use a generator
'''


def is_prime(n):
    '''Checks if a given number is a prime number'''
    if n <= 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(3, int(n ** 0.5), 2):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    if n < 2:
        return 2
    # using a generator for this problem seems very wrong. why not while True > increment by 1??
    for num in range(n + 1, n * 2):
        if is_prime(num):
            break
    return num


def main2():
    print(first_prime_over())


if __name__ == "__main__":
    main2()
