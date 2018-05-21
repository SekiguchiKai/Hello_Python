class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_my_name(self):
        print("My name is {0}".format(self.name))

    def say_my_age(self):
        print("My age is {0}".format(self.age))


class Cat(Animal):
    def __init__(self,name, age, kind):
        super().__init__(name, age)
        self.kind = kind

    def say_my_kind(self):
        print("I am {0}".format(self.kind))


tama = Cat("タマ", 10, "三毛猫")
tama.say_my_name()
tama.say_my_age()
tama.say_my_kind()
