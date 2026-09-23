# Begin1. Дана сторона квадрата a. Найти его периметр P = 4·a.
a = float(input())
perimeter = 4 * a
print(perimeter)

# Begin2. Дана сторона квадрата a. Найти его площадь S = a2.
a = float(input())
area = a ** 2
print(area)

# Begin3. Даны стороны прямоугольника a и b.
# Найти его площадь S = a·b и периметр P = 2·(a + b).
a = float(input())
b = float(input())
area = a * b
perimeter = 2 * (a + b)
print(area)
print(perimeter)

# Begin4. Дан диаметр окружности d. Найти ее длину L = π·d.
d = float(input())
pi = 3.14
length = pi * d
print(length)

# Begin5. Дана длина ребра куба a.
# Найти объем куба V = a3 и площадь его поверхности S = 6·a2.
a = float(input())
volume = a ** 3
surface = 6 * a ** 2
print(volume)
print(surface)