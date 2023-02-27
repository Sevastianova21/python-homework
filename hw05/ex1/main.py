# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def degree(a,b):
    if b == 1:
        return a
    return degree(a, b - 1) * a
a,b = input('Введите числа А и В через запятую ').split(',')
print(degree(int(a),int(b)))
