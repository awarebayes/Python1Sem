# Посторить таблицы функции
# _________________________
# |  x  |    f1   | f2    |
# Определить min t1, t2
# Постороить график одной из функций,
# на оси необходимо поставить от 4 до 8 засечек пользователя
#  Написал: Щербина МА ИУ7  15Б

from math import inf, ceil

N_FUN = 2  # number of functions
COL_W = 15  # number of symbols per column

# input all the things we need
start = float(input(">>> range start (float): "))
end = float(input(">>> range end (float): "))
if start > end:
    print(f"Start should be less than end, got start ({start}) > end ({end})")
    exit(1)
step_size = float(input(">>> range step (float): "))

n_steps = ceil((end - start) / step_size) + 1

min_f1 = inf
min_f2 = inf
max_f1 = -inf
max_f2 = -inf

print("-" * (3 * COL_W + 4))

# 15 should be COL_W
# cant do dynamic formatting without double format...
print("|{:^15}|{:^15}|{:^15}|".format("x", "f1", "f2"))
for step in range(n_steps):
    x = start + step * step_size
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
PLOT_W = 100  # plot width

n_func = int(
    input("which function do you want to plot [1,2]? \n >>> ")
)  # which function to plot
y_ticks = int(
    input("how many ticks do you want on the y axis [4, 8]? \n >>> ")
)  # number of ticks on y axis
y_ticks -= 1
y_should_tick1 = 0  # when number should be placed
y_should_tick2 = 0  # when tick should be placed

if n_func == 1:
    f_min = min_f1
    f_max = max_f1
    f_range = max_f1 - min_f1

else:
    f_min = min_f2
    f_max = max_f2
    f_range = max_f2 - min_f2

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
print("  -> y")


# x axis
for step in range(n_steps):
    x = start + step * step_size
    if n_func == 1:
        y = x - 0.5 ** x
    else:
        y = x ** 3 - 4.49 * x ** 2 - 24.5 * x + 19.5
    percent_y = (y - f_min) / f_range  # where y is in range, normalized between [0, 1]
    pos_y = int(percent_y * PLOT_W)  # where y is in [0, PLOT_W]
    if pos_y == 0:  # y is on the x axis
        print("{:>6.2f}".format(x), "*", sep="")
    else:
        print("{:>6.2f}".format(x), "|", " " * (pos_y - 1), "*", sep="")
print(" " * 6 + "|")
print(" " * 6 + "v")
print(" " * 6 + "x")
