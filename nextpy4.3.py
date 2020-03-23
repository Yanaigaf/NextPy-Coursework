'''
4.3.4
Define function get_fibo() which returns a generator of fibonacci sequence
'''


def get_fibo(max=1):
    x, y = 0, 1
    yield x
    while y <= max:
        yield y
        x, y = y, x + y


for i in get_fibo(564573):
    print(i)
