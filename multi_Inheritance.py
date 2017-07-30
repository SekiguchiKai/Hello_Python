import time


class Parent1:

    def __init__(self, name):
        self._name = name

    def show_my_name(self):
        print("My name is {0}.".format(self._name))

    def call(self):
        print("Hello, I'm {0}.".format(self._name))


class Parent2:

    def __init__(self, name):
        self._name = name

    def show_my_name(self):
        print("私の名前は{0}です。".format(self._name))

    def say_time(self):
        print("現在の時刻は{0}".format(time.ctime()))


# Parent1, Parent2を多重継承
class Child(Parent1, Parent2):
    pass

child = Child("childインスタンス")
# 多重継承で継承した親classに同じメソッドが存在する場合、最初の方のclassのメソッドが継承される
child.show_my_name()
child.say_time()
child.call()

