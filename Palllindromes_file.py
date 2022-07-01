name_file = open('words.txt', 'r')
try:
    count_paldr = 0
    for i_line in name_file:
        whithout_n = i_line[:-1]
        reversed_string = ''.join(reversed(whithout_n))
        if reversed_string == whithout_n:
            count_paldr += 1
        if reversed_string.isdigit():
            raise TypeError
except TypeError:
    print('Только буквы!')
print(count_paldr)

name_file.close()