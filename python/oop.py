# https://realpython.com/python3-object-oriented-programming/

# Classes define functions called methods,
# which identify the behaviors and actions that an object created from the class can perform with its data.

# While the class is the blueprint, an instance is an object that is built from a class and contains real data.

# Python class names are written in CapitalizedWords notation by convention.

class Dog:
    # Class attributes
    # 무조건 초기화되어야 함
    species = "Canis Familiaris"
    tmp = [1, 2, 3]

    # Every time a new Dog object is created, .__init__() sets the initial state of the object by assigning the values of the object’s properties.
    def __init__(self, name, age) -> None:
        # Instance attributes
        self.name = name
        self.age = age

    # Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores.
    def __str__(self):
        return f"{self.name} is {self.age} yeras old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class Bulldog(Dog):
    pass


class JackRussellTerrier(Dog):
    # override
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


if __name__ == "__main__":
    # Creating a new object from a class is called instantiating an object.
    d1 = Dog("a", 7)
    d2 = Dog("a", 7)
    print(d1)
    print(d2)        # print address of instance
    print(d1.__dir__)
    print(Dog.__dir__)
    print(d1 == d2)

    #d1.species = "kim"
    print(Dog.species)
    print(d1.species)
    print(id(Dog.species), id(d1.species))
    # 위의 얘들은 다 같은 메모리 주소를 가리키는 데??
    # The key takeaway here is that custom objects are mutable by default.
    # An object is mutable if it can be altered dynamically.
    # https://stackoverflow.com/questions/58581743/why-does-modifying-a-class-attribute-doesnt-modify-an-object-attribute-in-pytho

    d1.tmp[0] = 10

    print(id(d1.name))
    print(id(d1.age))

    jack = JackRussellTerrier("jack", 4)
    tom = Bulldog("tom", 5)

    print(jack.name)
    print(type(jack))
    print(isinstance(jack, Dog))
    # jack은 dog의 객체이지만 bulldog의 객체는 아니다
    # 자식 클래스에서 생성된 모든 객체는 부모 클래스의 인스턴스이다.
