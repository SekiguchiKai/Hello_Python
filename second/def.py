def calc_tax(amount):
    print("消費税は{0}円です".format(int(amount * 0.08)))

calc_tax(100)

def calc_price_including_tax(amount):
    return int(amount * 1.08)

amount = 100
price_including_tax = calc_price_including_tax(amount)
print("100円の税込み金額は{0}円です。".format(price_including_tax))