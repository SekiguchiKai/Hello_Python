# クラス
class Phone:
    # コンストラクタ
    def __init__(self, number):
        self.__number = number

    # Pythonのメソッドは必ず1つの引数を持つらしい
    # 第一引数は、必ずselfにするのが慣習らしい
    def show_my_number(self):
        print('This phone\'s number is{0}.'.format(self.__number))

    # Pythonのメソッドは必ず1つの引数を持つらしい
    # 第一引数は、必ずselfにするのが慣習らしい
    def call(self, phone_partner):
        print('Call to {0}.'.format(phone_partner))


# Phoneの子クラス
class SmartPhone(Phone):
    def __init__(self, number, os):
        super().__init__(number)
        self.os = os

    # Overrideした
    def call(self, phone_partner):
        print('Video call to {0}.'.format(phone_partner))

    def show_my_os(self):
        print('This phone\'s os is {0}.'.format(self.os))

    # クラスメソッド
    @classmethod
    def take_a_picture(cls, subject):
        print('Take a picture of {0}'.format(subject))

print("===Normal Phone===")
normalPhone = Phone("xxx-xxx-xxx")
normalPhone.show_my_number()
normalPhone.call("sekky0905")

print("===Smart Phone===")
iPhone = SmartPhone("○○○-○○○-○○○", 'ios')
iPhone.show_my_number()
# Phoneを継承しているから使える
iPhone.call("sekky0905")
iPhone.show_my_os()
# クラスメソッド
SmartPhone.take_a_picture("flower")




