# Напишите функцию square, принимающую один аргумент — сторону квадрата — и возвращающую площадь квадрата.

def square(side):
    return side ** 2

side_length = 6
area = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {area}")