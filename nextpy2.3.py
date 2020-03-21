# 2.3.3 take the animal class from 2.2 and add:
# "hide" class inner attributes with _
# default name to Octavio
# add set_name method to change animal name
# add get_name method to return animal name
# add variable count_animals to count how many instance of the class have been made. where should this go?
# in main instantiate the class twice: once with a name and once without
# print the names of both instances
# change the name of one of the class instances then print it again
# print count_animals and verify that it is equal to 2

# bonus - I made name and age in properties


class Octopus:
    _count_animals = 0

    def __init__(self, age=0, name='Octavio'):
        self.name = name
        self.age = age
        self.__class__._count_animals += 1

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, val):
        if hasattr(self, 'name'):
            print(f'{self.name} is now called {val}')
        else:
            print(f'New pet! hi {val}!')
        self._name = val

    @age.setter
    def age(self, val):
        print(f'{self.name} is {val} years old')
        self._age = val

    @classmethod
    def get_num_animals(cls):
        return cls._count_animals

    def birthday(self):
        print(f"happy birthday {self.name}!")
        self.age += 1

    def __repr__(self):
        return self.name


if __name__ == "__main__":
    print(f"{'2.3.3':-^50}")
    octo1 = Octopus(2)
    octo2 = Octopus(4, 'richard')
    octo1.birthday()
    print(f'{octo1.name} is {octo1.age} years old, {octo2.name} is {octo2.age} years old')
    octo1.name = 'courtney'
    print(octo1.name)
    print("Number of animals we have:", Octopus.get_num_animals())  # should print 2 since we created 2 animals
    print(f"{'':-^50}")


# 2.3.4
# 1 - Create a pixel class used to describe pixels on a screen.
#     each pixel hold its location in x, y coordinates and its color in RGB scale. All will default to 0
# 2 - apply a set_coords method and a set_grayscale method (grayscale is defined by averaging the values of RGB
#     and setting it to all pixels)
# 3 - apply print_pixel_info method to print all values of the pixel, plus its color
#     in text if all but 1 of RGB are 0


class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self.set_coords(x, y)
        self._update_pixels(red, green, blue)

    def _update_pixels(self, *args):
        self._red = self._check_pixel(args[0])
        self._blue = self._check_pixel(args[1])
        self._green = self._check_pixel(args[2])
        self.RGB = {'Red': self._red, 'Green': self._green, 'Blue': self._blue}

    def _check_pixel(self, value):
        if value > 255 or value < 0:
            raise ValueError("Pixel RGB color has to be between 0 and 255")
        return value

    def set_coords(self, x, y):
        print(f"setting coords to x={x} y={y}")
        self._x = x
        self._y = y

    def set_grayscale(self):
        color = round(((self._red + self._green + self._blue) / 3), 3)
        self._update_pixels(color, color, color)

    def print_pixel_info(self):
        rgb = tuple(self.RGB.values())
        pixel = f'X: {self._x}, Y: {self._y}, Color: {rgb}'
        count_zeros = 0
        for k, v in self.RGB.items():
            if v == 0:
                count_zeros += 1
            else:
                key = k
        if count_zeros == 2:
            pixel += ' ' + key
        print(pixel)


if __name__ == "__main__":
    print(f"{'2.3.4':-^50}")
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.set_coords(9, 4)
    p.print_pixel_info()
    print(f"{'':-^50}")
