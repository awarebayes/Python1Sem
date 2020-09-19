# По заданным параметрам фигуры определить объем и характеристики
# Пяти угольный призма вписанна в цилиндр
# Ввод: радиус, высота призмы
# Вывод: Бок площадь, объем
# Автор: Щербина МА ИУ7 15 Б
import math as m


def main():
    print("Volume / Side Area of an Inscribed Prism")

    r = float(input(">>> radius (float): "))  # радиус
    h = float(input(">>> height (float): "))  # высота

    if r < 0 or h < 0:
        print("radius and height should be positive!")
        exit(1)

    base_side = 2 * r * m.sin(m.radians(36))  # сторона основания
    base_area = 0.5 * r * r * 5 * m.sin(m.radians(72))  # площадь основания

    print("Prism side area: {:g}".format(base_area * h), "(units squared)")
    print("Prism volume: {:g}".format(5 * base_side * h), "(units cubed)")


if __name__ == "__main__":
    main()
