# class名の頭文字は大文字
class Lang:
    pass

# こういう書き方もできるらしい
java = Lang()
java.name = "Java"
java.type = "Static"

print(java.name + "は" + java.type)

python = Lang()
python.name = "Python"
python.type = "Dynamic"
python.since = 1991
print("{0}は{1}で{2}年からある".format(python.name, python.type, python.since))


# コンストラクタ
class Person:
    # コンストラクタの書き方はこうらしい
    # self = this
    def __init__(self, name):
        self.name = name

sekky = Person("Sekky")
print(sekky.name)

# 以下は当然エラーになる
# sekky0905 = Person()
# print(sekky0905.name)


