# 2.4.2 create a class BigThing which receives 1 argument on creation
# 1 - class has a method size() which returns the argument if its a number or it's length otherwise
# 2 - define a class BigCat which inherits from BigThing and receives an extra argument weight.
#     calling BigCat.size shall return 'fat' if weight > 15, 'very fat' if weight > 20 or 'OK' otherwise

# bonus - I added a name_size method to BigCat which will call the deafult size method of BigThing


class BigThing:
    def __init__(self, value):
        self._thing = value

    def size(self):
        if hasattr(self._thing, '__len__'):
            return len(self._thing)
        else:
            return self._thing


class BigCat(BigThing):
    def __init__(self, value, weight):
        super().__init__(value)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "very fat"
        elif self._weight > 15:
            return "fat"
        else:
            return "OK"

    def name_size(self):
        return super().size()


if __name__ == "__main__":
    print(BigThing(6.4).size(), BigThing('hello').size(), BigThing([1, 2, 3]).size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size(), cutie.name_size())
