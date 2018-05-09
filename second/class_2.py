class Person:
    # class変数(同一classから生成した全部のインスタンスで共通の値を持つ)
    count = 0
    # コンストラクタ
    def __init__(self, name):
        # class変数へのアクセス方法は、インスタンス変数とは異なるので注意!
        # インスタンス化の度に+1されるようにする
        Person.count += 1
        # インスタンス変数
        self.name = name



sekky = Person("sekky")
print(sekky.name)
print(sekky.count)

taro = Person("太郎")
print(taro.name)
print(taro.count)