class Animal:
    """
    A class for storing animals

    class attributes:
        animals: (list) to store all animals
    instance attributes:
        name:  (str) to store animal name
        number: (int) to store animal order number (starting with 1)

    class methods:
        __str__: string representation of animal, e.g. "1. Dog"

    static methods:
        zoo: returns string representation of all animals in orderd lies, e.g.
           '''\
           1. Dog
           2. Cat'''
    """
    # YOUR CODE HERE
    animals = []

    def __init__(self, name):
        self.name = name
        self.number = len(Animal.animals) + 1
        Animal.animals.append(self)

    def __str__(self):
        return f"{self.number}. {self.name}"

    @staticmethod
    def zoo():
        return '\n'.join(str(animal) for animal in Animal.animals)

    ################


Animal.animals.clear()
dog = Animal("dog")
print(dog.__str__())

cat = Animal("cat")
# cat.number = 2
print(cat.__str__())