class Person:
    # コンストラクタ
    def __init__(self, name):
        # アンダーバー2つでprivate
        self.__name = name



sekky = Person("sekky")
# privateにしてもこう言う書き方だとアクセスできちゃう
print(sekky._Person__name)