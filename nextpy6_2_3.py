'''
import both previous files.
instantiate each class once and call greeting_msg
'''

import nextpy6_2_1
import nextpy6_2_2


def main():
    greeting = nextpy6_2_1.GreetingCard()
    birthday = nextpy6_2_2.BirthdayCard(sender_age=19)
    greeting.greeting_msg()
    birthday.greeting_msg()


if __name__ == "__main__":
    main()
