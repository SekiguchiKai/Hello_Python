def calc_tax(value, tax_rate=0.08):
    print("{0}円の税込価格は、{1}円".format(value, value + value * tax_rate))

calc_tax(100, 0.03)
calc_tax(100, 0.05)
calc_tax(100)


# 関数を返値にできるよ
def return_calc_tax(value, tax_rate=0.08):
    return calc_tax(value, tax_rate)

return_calc_tax(100, 0.03)
return_calc_tax(100, 0.05)
return_calc_tax(100)


# 何もしないということをpassで現わせるらしい
def return_pass():
    pass

print(return_pass())


