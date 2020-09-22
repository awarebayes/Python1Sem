# Написать решение квадратного уравнения по коэффициентам
# Ввод: коефициенты a,b,c
# Вывод: корни (или корень) (или нет корней)
# Написал: Щербина Михаил 15Б

print("Solving: a*x^2 + b*x + c = 0")
a = float(input(">> a (float): "))  # x**2 term
b = float(input(">> b (float): "))  # x term
c = float(input(">> c (float): "))  # free term

if a == 0:
    # Линейное уравнение
    if b == 0:
        if c == 0:
            print("Any x can be solution")
        else:
            print("No solutions exist")
    else:
        x = -c / b
        print("Only root x: {:g}".format(x))
else:
    # Квадратное уравнение
    D = b ** 2 - 4 * a * c  # дискриминант
    if D < 0:
        print("No solutions exist")
    else:
        if D == 0:
            x = -b / (2 * a)  # единственный корень
            print("Only root x: {:g}".format(x))
        else:
            x1 = (-b + D ** (1 / 2)) / (2 * a)
            x2 = (-b - D ** (1 / 2)) / (2 * a)
            print("Root x1: {:g}".format(x1))
            print("Root x2: {:g}".format(x2))
