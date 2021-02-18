import math
number_apartment = int(input())
floor = int(input())
count_apartments = int(input())
all_apartments = floor * count_apartments


def flat_position():
    if number_apartment <= all_apartments:
        entrance = 1
        floor_1 = number_apartment // count_apartments
    else:
        entrance = math.ceil(number_apartment / all_apartments)
        floor_1 = ((number_apartment - all_apartments) // count_apartments)
    return print('Подъезд:' + str(entrance) + ' ' + 'Этаж:' + str(floor_1))


flat_position()
