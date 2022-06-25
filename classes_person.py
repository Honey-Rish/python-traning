#packages

class Person:
    def __init__(self, name, age):
        self.name = name
        # Private attribute
        self.__age = age

    def getage(self):
        return self.__age


p1 = Person("Scott", 45)
print(p1.__dict__)
print(p1.getage())
print(p1.name, p1._Person__age)