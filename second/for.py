print("===Fizz Buzz====")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz!")
    elif i % 3 == 0:
        print("Fizz!")
    elif i % 5 == 0:
        print("Buzz!")
    else:
        print(i)


print("===奇数の時だけ表示====")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)