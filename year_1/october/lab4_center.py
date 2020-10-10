# Посторить таблицы функции
# _________________________
# |  x  |    f1   | f2    |
# Определить min f1, f2
# Постороить график одной из функций,
# на оси необходимо поставить от 4 до 8 засечек пользователя
#  Написал: Щербина МА ИУ7  15Б

from math import inf, ceil
from os import get_terminal_size
from math import log

N_FUN = 2  # number of functions
COL_W = 15  # number of symbols per column

# input all the things we need
start = float(input(">>> range start (float): "))
end = float(input(">>> range end (float): "))
if start > end:
    print(f"Start should be less than end, got start ({start}) > end ({end})")
    exit(1)
step_size = float(input(">>> range step (float): "))
max_exp = int(log(max(map(abs, [start, end])), 10))

n_steps = ceil((end - start) / step_size) + 1

min_f1 = inf
min_f2 = inf
max_f1 = -inf
max_f2 = -inf

print("-" * (3 * COL_W + 4))
# 15 should be COL_W
# cant do dynamic formatting without double format...
print("|{:^15}|{:^15}|{:^15}|".format("x", "f1", "f2"))
print("-" * (3 * COL_W + 4))
for step in range(n_steps):
    x = start + step * step_size
    if x > end:
        break
    f1 = x - 0.5 ** x
    f2 = x ** 3 - 4.49 * x ** 2 - 24.5 * x + 19.5
    print("|{:^15g}|{:^15g}|{:^15g}|".format(x, f1, f2))
    min_f1 = min(f1, min_f1)
    min_f2 = min(f2, min_f2)
    max_f1 = max(f1, max_f1)
    max_f2 = max(f2, max_f2)

print("-" * (3 * 15 + 4))

print()
print(f"min f1 is {min_f1:g}")
print(f"min f2 is {min_f2:g}")
print()

# Plotting Part!
# P.S. This is the actual plot size, not including axes and labels
PLOT_W, _ = get_terminal_size()  # plot width
PLOT_W -= 15  # adjust to fit better

# n_func = int(
#    input("which function do you want to plot [1,2]? \n >>> ")
# )  # which function to plot
y_ticks = int(
    input("how many ticks do you want on the y axis [4..8]? \n >>> ")
)  # number of ticks on y axis
y_ticks -= 1
y_should_tick1 = 0  # when number should be placed
y_should_tick2 = 0  # when tick should be placed


f_min = min(min_f1, min_f2)
f_max = max(max_f1, max_f2)
f_range = f_max - f_min


# y axis - number labels
print(" " * 6, end="")
i = 0
while i < PLOT_W + 1:  # +1 is to print the last nu,ber / tick
    if i + 1 > y_should_tick1:
        y_should_tick1 += PLOT_W / y_ticks  # update tick
        y_val = f_min + f_range * (i / PLOT_W)  # value of y at i
        y_fmt = "{:.2f}".format(y_val)  # y formatted
        i += len(y_fmt)
        print(y_fmt, end="")
    else:
        print(" ", end="")
        i += 1

print()

# y axis - axis and ticks
print(" " * 6, end="")
for i in range(PLOT_W + 1):  # +1 is to print the last nu,ber / tick
    if i + 1 > y_should_tick2:
        y_should_tick2 += PLOT_W / y_ticks  # update tick
        print("|", end="")  # tick
    else:
        print("-", end="")  # axis
print("--->y")

x_axis_zero = int((-f_min / (f_max - f_min)) * PLOT_W)  # where x axis should be
x_axis_exists = f_min <= 0 <= f_max

# x axis
for step in range(n_steps):
    x = start + step * step_size

    # function 1
    y1 = x - 0.5 ** x
    percent_y1 = (
        y1 - f_min
    ) / f_range  # where y1 is in range, normalized between [0, 1]
    pos_y1 = int(percent_y1 * PLOT_W)  # where y2 is in [0, PLOT_W]

    # function 2
    y2 = x ** 3 - 4.49 * x ** 2 - 24.5 * x + 19.5
    percent_y2 = (
        y2 - f_min
    ) / f_range  # where y2 is in range, normalized between [0, 1]
    pos_y2 = int(percent_y2 * PLOT_W)  # where y2 is in [0, PLOT_W]

    x = x / 10 ** max_exp  # make x into exponent
    print("{:>6.2f}|".format(x), sep="", end="")  # right label

    for i in range(PLOT_W + 1):
        if i == pos_y1:
            print("‣", end="")
        elif i == pos_y2:
            print("•", end="")
        elif i == x_axis_zero and x_axis_exists:
            print("|", end="")
        else:
            print(" ", end="")
    print()

if x_axis_exists:
    x_label_pos = x_axis_zero + 7  # where x axis label should be
    print(" " * x_label_pos + "|")
    print(" " * x_label_pos + "v")
    print(" " * x_label_pos + "x*10^", max_exp, sep="")
