'''
4.4
1 - define fuction gen_secs which returns a generator of possible seconds (0 to 59)
2 - define a fuction gen_minutes which returns a generator of possible minutes (0 to 59)
3 - define a function gen_hours which returns a generator of possible minuts (0 to 23)
4 - define a fuction gen_time which returns a generator of all possible times of day in format HH:MM:SS.
5 - define a function gen_years(start) with start defaulting to current year which returns a generator of all possible years starting from start
6 - define a function gen_months() which returns a generator of all possible months (1 to 12)
7 - define a function gen_days(month, leap_year=true) which returns a generator of all possible days in given month
8 - define a function gen_date() which returns a generator of all dates in the format dd/mm/yyyy hh:mm:ss
9 - iterate over gen_date and print the result every 1000000 iterations
'''


def gen_secs():
    for sec in range(0, 60):
        yield sec


def gen_minutes():
    for min in range(0, 60):
        yield min


def gen_hours():
    for hour in range(0, 24):
        yield hour


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f'{hour:02d}:{minute:02d}:{second:02d}'


def gen_years(start=2020):
    while True:
        yield start
        start += 1


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        # definition of a leap year
        leap_year = True
    else:
        leap_year = False
    for day in range(1, 29):
        yield day
    if month != 2 or leap_year:
        day += 1
        yield day
    if month != 2:
        day += 1
        yield day
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day += 1
        yield day


def gen_date(start_year=2020):
    for year in gen_years(start_year):
        for month in gen_months():
            for day in gen_days(month, year):
                for time in gen_time():
                    yield f'{year}/{month:02d}/{day:02d} {time}'


def main():
    n = 0
    for date in gen_date(2030):
        n += 1
        if n % 1000000 == 0:
            print(date)


if __name__ == "__main__":
    main()
