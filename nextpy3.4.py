"""
Exercise 3.4
Checking login credentials:
Username - can include uppercase, lowercase, digits and '_' only. must be 3-16 characters
Password - must be 8-40 characters. Must include at least 1 uppercase, 1 lowercase, 1 digit, and 1 special characters
1 - Define a check_input function - input username, password - return "OK" if pass all checks
2 - Define an exception for each constraint
3 - raise exception in check_input if constraint has not been met
4 - write main function that will keep prompting user for input until both inputs pass
5 - Improve UsernameContainsIllegalCharacters so show index of bad char and improve PasswordMissingCharacter to show what type of char is missing
"""


import string

lcase = set(string.ascii_lowercase)
ucase = set(string.ascii_uppercase)
punc = set(string.punctuation)
dig = set(string.digits)
allowed_user = lcase | ucase | dig | set('_')


class UsernameTooShort(Exception):
    def __str__(self):
        return "Username is too short"


class UsernameTooLong(Exception):
    def __str__(self):
        return "Username is too long"


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username):
        missing = set(username).difference(allowed_user)
        for c in username:
            if c in missing:
                self.badchar = c
                break
        self.index = username.index(self.badchar)

    def __str__(self):
        return f"Username contains illegal character {self.badchar!r} at index {self.index}"


class PasswordTooShort(Exception):
    def __str__(self):
        return "Password is too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "Password is too long"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "Password missing a required character"


class PasswordMissingLower(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingUpper(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special character)"


def check_input(username, password):
    username_set = set(username)
    password_set = set(password)
    try:
        if len(username) < 3:
            raise UsernameTooShort
        if len(username) > 16:
            raise UsernameTooLong
        if len(password) < 8:
            raise PasswordTooShort
        if len(password) > 40:
            raise PasswordTooLong
        if not allowed_user.issuperset(username_set):
            raise UsernameContainsIllegalCharacter(username)
        if password_set.isdisjoint(lcase):
            raise PasswordMissingLower
        elif password_set.isdisjoint(ucase):
            raise PasswordMissingUpper
        elif password_set.isdisjoint(dig):
            raise PasswordMissingDigit
        elif password_set.isdisjoint(punc):
            raise PasswordMissingSpecial
    except Exception as e:
        print(e)
    else:
        print("OK")
        return True
    finally:
        del username_set
        del password_set
        del username
        del password


def main():
    while True:
        username = input("Enter username\n")
        password = input("Enter password\n")
        if check_input(username, password):
            break


if __name__ == "__main__":
    main()

# TODO This could be adapted to a full-fledged python module by creating a user-customizable Policy class and checking everything against it's properties
