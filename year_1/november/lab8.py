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
from utils import fool_proof_float_input, fool_proof_int_input


# function for you to mess with
def f(x):
    return x + 5


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
    first_start = start  # where we started first
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
    start = 0
    end = 10

    # it is called "encapsulation"
    left_rectangles = lambda parts: integrate_left_rect(f, start, end, parts)
    weddle = lambda parts: integrate_weddle(f, start, end, parts)

    # input
    # can replace int(input(...)) with fool_proof_int_input(...)
    parts_1 = fool_proof_int_input(">>> 1st number of partitions: ")
    parts_2 = fool_proof_int_input(">>> 2nd number of partitions: ")

    if parts_1 <= 0 or parts_2 <= 0:
        print("Must be positive!")
        exit(1)

    # integration results
    res_1_left = left_rectangles(parts_1)
    res_2_left = left_rectangles(parts_2)
    res_1_weddle = weddle(parts_1)
    res_2_weddle = weddle(parts_2)

    # table formatting, can you not read the function name?
    print()
    pprint_table(
        [
            "Method",
            "Left Rectangles",
            "Weddle",
        ],
        [f"N Partitions: {parts_1}", res_1_left, res_1_weddle],
        [f"N Partitions: {parts_2}", res_2_left, res_2_weddle],
        margin=2,
    )
    print()

    print("Left rectangles required is less prescise")
    # can replace float(input(...)) with fool_proof_float_input(...)
    prec = fool_proof_float_input(">>> prescision for left rectangles: ")

    left_target_parts, end_res = search_parts_prescision(left_rectangles, prec)

    print(f"It takes {left_target_parts} partitions to calculate with that prescision")
    print(f"End result is: {end_res:.8f}")


main()
