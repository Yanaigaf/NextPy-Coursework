"""2.5 - "mid-term" course assignment
"""
# 1
# Define an Animal class with attributes _name(no default) and _hunger(default 0)
# bonus - I defined these attributes as properties


class Animal:
    """A class used to represent an animal"""

    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """Initialize the animal class\n
        :param name: name of animal, type str\n
        :param hunger: animal's starting hunger, type int, default 0\n
        :raise: ValueError if param types do not match requirement"""

        self.name = name
        self.hunger = hunger

    @property
    def name(self):
        """getter function for name attribute\n
        :return: animal name, type str"""

        return self._name

    @name.setter
    def name(self, name):
        """setter function for name attribute\n
        :param name: animal name, type str\n
        :raise: ValueError if param is not str\n
        :return: None"""

        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Animal name must be a string")

    @property
    def hunger(self):
        """getter function for hunger attribute\n
        :return: animal hunger, type int"""

        return self._hunger

    @hunger.setter
    def hunger(self, hunger):
        """setter function for hunger attribute\n
        :param value: animal hunger, type int\n
        :raise: ValueError if param is not int\n
        :return: None"""

        if isinstance(hunger, int):
            self._hunger = hunger
        else:
            raise TypeError("Animal hunger must be of type int")

    def is_hungry(self):
        """Checks if the animal is hungry or not\n
        :return: True or False, type bool"""

        if self.hunger > 0:
            return True
        else:
            return False

    def feed(self):
        """Feeds the animal, reducing its hunger by one\n
        :return: None"""

        self.hunger -= 1

    def talk(self, speech="I am an animal"):
        """Prints animal's speech to screen\n
        :param speech: speech to print, type str\n
        :raise: ValueError if speech isn't string"""

        if isinstance(speech, str):
            print(speech)
        else:
            raise TypeError("Speech must be of type str")

    def __repr__(self):
        return "Animal"

# 2
# Define subclasses that inherit from Animal for the following types: Dog, Cat, Skunk, Unicorn, and Dragon


class Dog(Animal):
    """A class used to represent a dog"""

    def __repr__(self):
        return "Dog"

    def talk(self):
        """The dog talks"""

        super().talk("woof woof")

    def fetch_stick(self):
        """The dog fetches a stick"""

        super().talk("There you go, sir!")


class Cat(Animal):
    """A class used to represent a cat"""

    def __repr__(self):
        return "Cat"

    def talk(self):
        """The Cat talks"""

        super().talk("Meow")

    def chase_laser(self):
        """The cat chases a laser pointer"""

        super().talk("Meeeeeow")


class Skunk(Animal):
    """A class used to represent a skunk"""

    def __init__(self, name, hunger, stink_count=6):
        """Initialize the Skunk class\n
        :param name: name of Skunk, type str\n
        :param hunger: Skunk's starting hunger, type int, default 0\n
        :param stink_count: Skunk's stink count, type int, default 6 \n
        :raise: ValueError if param types do not match requirement"""

        super().__init__(name, hunger)
        self.stink_count = stink_count

    @property
    def stink_count(self):
        """getter function for stink_count property\n
        :return: stink_count, type int"""

        return self._stink_count

    @stink_count.setter
    def stink_count(self, stink_count):
        """setter function for stink_count property\n
        :param stink_count: stink_count of the skunk, type int, default 6
        :raise: TypeError if stink_count isn't int"""

        if isinstance(stink_count, int):
            self._stink_count = stink_count
        else:
            raise TypeError("Stink count must be of type int")

    def __repr__(self):
        return "Skunk"

    def talk(self):
        """The Skunk talks"""

        super().talk("tsssss")

    def stink(self):
        """The skunk stinks"""

        super().talk("Dear lord!")


class Unicorn(Animal):
    """A class used to represent a unicorn"""

    def __repr__(self):
        return "Unicorn"

    def talk(self):
        """The Unicorn talks"""

        super().talk("Good day, darling")

    def sing(self):
        """The unicorn sings"""

        super().talk("I'm not your toy...")


class Dragon(Animal):
    """A class used to represent a dragon"""

    def __init__(self, name, hunger, color='Green'):
        """Initialize the Dragon class\n
        :param name: name of Dragon, type str\n
        :param hunger: Dragon's starting hunger, type int, default 0\n
        :param color: Dragon's color, type str, default Green\n
        :raise: ValueError if param types do not match requirement"""

        super().__init__(name, hunger)
        self.color = color

    @property
    def color(self):
        """getter function for color property\n
        :return: color, type str"""

        return self._color

    @color.setter
    def color(self, color):
        """setter function for color property\n
        :param color: color of the dragon, type str, default Green\n
        :raise: ValueError if color isn't string"""

        if isinstance(color, str):
            self._color = color
        else:
            raise TypeError("Dragon color must be of type str")

    def __repr__(self):
        return "Dragon"

    def talk(self):
        """The Dragon talks\n
        :return: speech, type str"""

        super().talk("Raaaawr")

    def breathe_fire(self):
        """The dragon breathes fire\n
        :return: speech, type str"""

        super().talk("$@$#$@$")


# 3
# Define methods: get_name (return _name), is_hungry (return True if _hunger>0), feed (_hunger -= 1)
# I added these methods to the parent Animal class


# 4
# Instantiate animal classes as follows in main:
# TYPE    NAME    HUNGER
# Dog     Brownie   10
# Cat     Zelda     3
# Skunk   Stinky    0
# Unicorn Keith     7
# Dragon  Lizzy    1450
#
# Save animals in a list zoo_lst
# iterate on zoo_lst and print animal type, name, and feed animal until it is not hungry


def main():
    zoo_lst = [Dog('Brownie', 10),
               Cat('Zelda', 3),
               Skunk('Stinky', 0),
               Unicorn('Keith', 7),
               Dragon('Lizzy', 1450),
               Dog('Doggo', 80),
               Cat('Kitty', 80),
               Skunk('Stinky Jr.', 80, 71),
               Unicorn('Clair', 80),
               Dragon('McFly', 80, 'Blue')
               ]
    for animal in zoo_lst:
        feed_count = 0
        while animal.is_hungry():
            animal.feed()
            feed_count += 1
        print(f'{animal} named {animal.name} has been fed {feed_count} times')
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
            print(animal.stink_count)
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breathe_fire()
            print(animal.color)
        print(animal.zoo_name)


if __name__ == "__main__":
    main()


# 5
# Apply polymorphism and add talk method to Animal and each of its subclasses. Each animal will say something else.
# after the print statement added to main in #4, add an extra print statement that will call talk method

# 6
# Each class has its own unique method. implement it then call it after calling talk in main

# 7
# add attributes _stink_count(default 6) to skunk and _color(default green) to dragon

# 8
# Add 1 new animal of each type to zoo_lst BEFORE the loop portion of main

# 9
# add zoo_name "Hayaton" to Animal class. this is a class wide property. Print it at the end of main
