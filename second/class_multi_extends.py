class Hoge:
    def say_hoge(self):
        print("Hoge~")

    def say_my_class_name(self):
        print("my class name is Hoge~")


class Foo:
    def say_foo(self):
        print("Foo~")

    def say_my_class_name(self):
        print("my class name is Foo~")


class Bar(Hoge, Foo):
    pass


b = Bar()
b.say_hoge()
b.say_foo()

# 多重継承で同じメソッドがる場合は、class Bar(Hoge, Foo):で先に書かれた方が優先
b.say_my_class_name()
