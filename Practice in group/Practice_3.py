txt = open('numbers.txt', 'r')  # в файле теперь file descriptor

sum_numbers = 0
for line in txt:  # для каждой строки в файле
    new_line = "".join(c for c in line if c not in ';')
    list_1 = new_line.split()  # строку из файла формируем в список
    count = list_1[:-2]
    count_1 = list(map(int, (list_1[-2:])))
    new_line2 = "".join(c for c in line if c not in '\n')
    print(new_line2)

    # print(count_1)

    for i in count:
        sum_numbers += int(i)
    # print(sum_numbers)
    average = sum_numbers // len(count)
    # print(average)
    average_1 = sum_numbers % len(count)
    # print(average_1)
    average_list = [average, average_1]
    # print(average_list)
    print(average_list == count_1)
    print('\n')
    sum_numbers = 0
