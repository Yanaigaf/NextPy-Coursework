# 2.2.2 define a basic animal class and instantiate it twice
class Octopus:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    def __repr__(self):  # not required by course
        return self.name


if __name__ == "__main__":
    octavio = Octopus('octavio', 2)
    richard = Octopus('richard', 4)
    octavio.birthday()
    print(f'{octavio} is {octavio.get_age()} years old, {richard} is {richard.get_age()} years old')
