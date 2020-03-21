"""
3.3.2
Create exception named UnderAge
overwrite __str__ to say user is under 18, add his current age and how many years until he is 18.
throw exception by replacing line 3 in sample code
sample code:
def send_invitation(name, age):
    if int(age) < 18:
        print("under age")
    else:
        print("You should send an invite to " + name)

catch exception in code
run function with parameters 17 and 20
"""


class UnderAge(Exception):
    def __init__(self, age):
        self._age = age

    def __str__(self):
        remainder = 18 - self._age
        return f"You must be 18. you are currently {self._age}. Try again in {remainder} {'years' if remainder > 1 else 'year'}."


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(int(age))
    except ValueError as e:
        print(e)
    except UnderAge as e:
        print(e)
    else:
        print("You should send an invite to " + name)


def main():
    send_invitation('Bob', 17)
    send_invitation('Shelly', 20)
    send_invitation('Roger', '15')
    send_invitation('Dan', 'aaaa')


if __name__ == "__main__":
    main()
