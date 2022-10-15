print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a != 0:

    D = b ** 2 - 4 * a * c;
    print("Дискриминант D = %.2f" % D)
    if D > 0:
        import math

        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif D == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("нет корней")
else:
    print('долбаеб у тебя а == 0')