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
