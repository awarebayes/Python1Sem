"""
# Интегралы
# написал Щербина МА Иу7 15
# метод Уэддля, метод левых прямоугольникоv
Лаба состоит из 2х частей.
Первая часть.
Задаешь два числа: количество разбиений 1, количество разбиений 2. 
Считаешь своим методом на одном количестве, на втором. 
Метода у тебя 2. 
В итоге получается таблица вида
N1                  N2
M1       Value       Value
M2     Value        Value
Вторая часть.
Для менее точного метода из первой части
вводится точность и ищем, сколько должно быть разбиений исходного отрезка, чтобы достигнуть этой точности.
Т.е. мы берем N = 1  и N = 2. Смотрим разницу. Если точность не достигнута, то учащаем сетку разбиений в 2 раза, т.е. N = 2, N = 4.
И так итерационно, пока не достигнем нужно точности . 
Выводим значение приближенное интеграла и количества участков.
"""

from math import sin, ceil
from utils import pprint_table

# if need fool proof input:
# from utils import fool_proof_float_input, fool_proof_int_input


# function for you to mess with
def f(x):
    return x ** 2 + sin(x)


# implemenation of left triangle rule
def integrate_left_rect(f, start, finish, n_part):
    step = (finish - start) / n_part
    i = start
    integral = 0
    while i < finish:
        integral += step * f(i)
        i += step
    return integral


# implementation of weddle's method
def integrate_weddle(f, start, finish, n_part):
    if n_part % 6 != 0:
        n_part = ceil(n_part / 6) * 6
    step = (finish - start) / n_part  # step size
    first_start = start  # where we started furst
    integral = 0  # end integral
    for i in range(int(n_part / 6)):
        start = first_start + i * step * 6
        # plain up formula
        integral += (
            f(start + step * 0)
            + 5 * f(start + step * 1)
            + f(start + step * 2)
            + 6 * f(start + step * 3)
            + f(start + step * 4)
            + 5 * f(start + step * 5)
            + f(start + step * 5)
        )
    integral *= 3 / 10 * step
    return integral


# search number of partitions required for reaching the prescision
def search_parts_prescision(integral, prescision):
    parts = 2
    integrated = integral(parts)  # plain number of partitions
    integrated_double = integral(parts * 2)  # double the partitions
    parts *= 2
    # binary search upwards:
    while abs(integrated - integrated_double) > prescision:
        integrated = integrated_double
        integrated_double = integral(parts * 2)
        parts *= 2
    return parts, integrated_double


def main():
    start = 1
    end = 10

    # it is called "encapsulation"
    left_rectangles = lambda parts: integrate_left_rect(f, start, end, parts)
    weddle = lambda parts: integrate_weddle(f, start, end, parts)

    # input
    # can replace int(input(...)) with fool_proof_int_input(...)
    left_parts = int(input(">>> number of partitions for left rectangle: "))
    weddle_parts = int(input(">>> number of partitions for weddle: "))

    # integration results
    res_left = left_rectangles(left_parts)
    res_weddle = weddle(weddle_parts)

    # table formatting, can you not read the function name?
    pprint_table(
        ["Method", "Left Rectangles", "Weddle"],
        ["N Partitions", left_parts, weddle_parts],
        ["Result", res_left, res_weddle],
        margin=2,
    )

    print("Left rectangles required is less prescise")
    # can replace float(input(...)) with fool_proof_float_input(...)
    prec = float(input(">>> prescision for left rectangles: "))

    left_target_parts, end_res = search_parts_prescision(left_rectangles, prec)

    print(f"It takes {left_target_parts} partitions to calculate with that prescision")
    print(f"End result is: {end_res:.8f}")


main()
