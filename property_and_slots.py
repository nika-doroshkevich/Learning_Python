class Cat:
    __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise AttributeError("Name can't be empty!")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 1 or value > 15:
            raise AttributeError("Age should be in 1-15")
        self._age = value

    def __repr__(self):
        return f'Cat(name={self.name}, age={self.age})'

    # def __setattr__(self, key, value):
    #     if key not in self.FIELD:
    #         raise AttributeError(f"Only allowed {self.FIELD}")
    #     if key == 'name' and not value:
    #         raise AttributeError("Name can't be empty!")
    #     if key == 'age' and (value < 1 or value > 15):
    #         raise AttributeError("Age should be in 1-15")
    #     self.__dict__[key] = value


if __name__ == '__main__':
    tom = Cat("Tom", 11)
    print(tom)
