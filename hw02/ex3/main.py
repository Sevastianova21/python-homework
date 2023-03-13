# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
number = int(input('Введите число '))
extent = 1
while extent <= number:
    print(extent)
    extent = extent*2
