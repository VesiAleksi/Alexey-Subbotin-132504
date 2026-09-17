from math import sqrt, cos
a = float(input("Введите первую сторону: "))
b = float(input("Введите вторую сторону: "))
ang = float(input("Введите градусную меру угла между ними: "))
c = sqrt(a**2 + b**2 - 2 * a * b * cos(ang))
print("Третья сторона равна ", int(c))