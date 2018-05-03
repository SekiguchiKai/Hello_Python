# String
s1 = "Python"
print(s1)
# \nは改行
s2 = "A\nB\nC"
print(s2)
# \tはtab
s3 = "A\tB\tC"
print(s3)

# 複数行にまたがる文章
s4 = """
I am learning Python, because I want to earn following skills.
1. Machine Learning
2. Data Analysis
Python is necessary for the above skills.
"""

print(s4)

# int
i = 5

# float
f = 10.5

# bool (大文字)
b = True

# 割り算 : /
x = 10
a = 10 / 3
print(a)


# 切り捨て : //
x = 10
a = 10 // 3
print(a)

print("ウェ〜イ!" * 3)

dynamic_lang = "Python"
static_lang = "Go"

print("動的言語 : %s, 性的言語 : %s" % (dynamic_lang, static_lang))
print("動的言語 : {0}, 性的言語 : {1}".format(dynamic_lang, static_lang))