# listの作成
numbers = [0, 1, 2, 3, 4, 5]
numbers.append(6)

for number in numbers:
    print(number)

for i, number in enumerate(numbers):
    print("{0}={1}".format(i, number))

