number = int(input())
star = '*'


if number <= 0 or number % 2 == 0:
    print('Введите другое число')
elif number >= 0 and number % 2 != 0:
    for a in range(1, number + 2, 2):
        indent = int((number - a) / 2)
        print(' ' * indent, str(star)*a)
    for i in range(number, 0, -2):
        indent_1 = int((number - i) / 2)
        print(' ' * indent_1, str(star) * i)

