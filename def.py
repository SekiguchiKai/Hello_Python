def calc_tax(value, tax_rate=0.08):
    print("{0}円の税込価格は、{1}円".format(value, value + value * tax_rate))

calc_tax(100, 0.03)
calc_tax(100, 0.05)
calc_tax(100)