class Lang:
    # クラス変数
    serial = 0

    # コンストラクタ
    def __init__(self, name, type):
        # インスタンス変数にする変数は、コンストラクタでこの形にする
        # privateにするときは、_1つ(これは監修だけで実際にはアクセスできちゃう)
        self._name = name
        # さらに厳密にprivateにするときは、_2つ
        self.__type = type
        # ここで、selfとしてはダメ
        Lang.serial += 1

    def show_name(self):
        print('名前は{0}'.format(self._name))

    def show_type(self):
        print('タイプは{0}'.format(self.__type))
    # クラスメソッドは、このアノテーションをつける
    @classmethod
    def show_sirial(cls):
        print('シリアルナンバーは{0}'.format(cls.serial))


java = Lang("Java", "Static")
Lang.show_sirial()
java.show_name()
java.show_type()
java.show_sirial()

python = Lang("Python", "Dynamic")
Lang.show_sirial()
python.show_sirial()
python.show_name()
python.show_type()

# privateアクセスの実験
print('privateアクセスの実験、 _nameは{0}'.format(java._name))
# __(アンダーバー2つ)の場合は、通常の方法ではアクセスすることができない
# 以下のコードはエラーになる
# print('privateアクセスの実験、 __typeは{0}'.format(java.__type))

# ただし、__(アンダーバー2つ)でもこれならば、アクセスできてしまう
print('privateアクセスの実験、 __typeは{0}'.format(java._Lang__type))

# privateアクセスは上記のように慣習的なものなので、、紳士協定的な感じである

