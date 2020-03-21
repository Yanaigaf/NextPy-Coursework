"""
3.1.3
Define a function that returns the error for each of these exceptions
StopIteration
ZeroDivisionError
AssertionError
ImportError
KeyError
SyntaxError
IndentationError
TypeError
"""


def throw_StopIteration():
    return StopIteration


def throw_ZeroDivision():
    return ZeroDivisionError


def throw_AssertionError():
    return AssertionError


def throw_ImportError():
    return ImportError


def throw_KeyError():
    return KeyError


def throw_SyntaxError():
    return SyntaxError


def throw_IndentationError():
    return IndentationError


def throw_TypeError():
    return TypeError


def main():
    print(throw_StopIteration())
    print(throw_ZeroDivision())
    print(throw_AssertionError())
    print(throw_ImportError())
    print(throw_KeyError())
    print(throw_SyntaxError())
    print(throw_IndentationError())
    print(throw_TypeError())


if __name__ == "__main__":
    main()
