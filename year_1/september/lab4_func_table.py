# Посторить таблицы функции
# _________________________
# |  x  |    f1   | f2    |
# Определить min t1, t2
# Постороить график одной из функций, 
# на оси необходимо поставить от 4 до 8 засечек пользователя
#  Написал: Щербина МА ИУ7  15Б

from math import inf, ceil

TAB_W = 42  # table width
N_FUN = 2  # number of functions
COL_W = int(TAB_W / N_FUN) - 1 # number of symbols per column

# input all the things we need
#start = float(input(">>> range start (float):"))
#end = float(input(">>> range end (float):"))
start = 0.1
end = 1.0
if start > end:
    print(f"Start should be less than end, got start ({start}) > end ({end})")
    exit(1)
# step_size = float(input(">>> range step (float):"))
step_size = 0.05

n_steps = ceil((end - start) / step_size) + 1

min_f1 = inf
min_f2 = inf
max_f1 = -inf
max_f2 = -inf

print("_"*TAB_W)

print(f"|{{:^{COL_W}}}|{{:^{COL_W}}}|{{:^{COL_W}}}|".format("x", "f1", "f2"))
for step in range(n_steps):
    x = start + step * step_size
    f1 = x - 0.5 ** x
    f2 = x**3 - 4.49 * x ** 2 - 24.5 * x + 19.5
    print(f"|{{:^{COL_W}g}}|{{:^{COL_W}g}}|{{:^{COL_W}g}}|".format(x, f1, f2))

    min_f1 = min(f1, min_f1)
    min_f2 = min(f2, min_f2)
    max_f1 = max(f1, max_f1)
    max_f2 = max(f2, max_f2)

print("_"*TAB_W, "\n")

print(f"min f1 is {min_f1:g}")
print(f"min f2 is {min_f2:g}")
print()

# Plotting Part!
# P.S. This is the actual plot size, not including axes and labels
PLOT_W = 60  # plot width

# n_func = int(input("which function do you want to plot [1,2]?"))  # which function to plot
# x_ticks = int(input("how many ticks do you want on the x axis [4, 8]?"))  # number of ticks on x axis
# y_ticks = int(input("how many ticks do you want on the y axis [4, 8]?"))  # number of ticks on y axis
y_ticks = 7
y_should_tick1 = 0  # when number should be placed
y_should_tick2 = 0 # when tick should be placed
n_func = 1

if n_func == 1:
    f_min = min_f1
    f_max = max_f1
    f_range = max_f1 - min_f1

else:
    f_min = max_f2
    f_max = min_f2
    f_range = max_f2 - min_f2

# y axis 1
print(" ", end="")
for i in range(PLOT_W):
    if i+1 > y_should_tick1:
        y_should_tick1 += PLOT_W / y_ticks
        y_val = f_min + f_range * (i / PLOT_W)
        print("{:.2f}".format(y_val), end="")
    else:
        print(" ", end="")
print()

# y axis 1
print(" ", end="")
for i in range(PLOT_W):
    if i+1 > y_should_tick2:
        y_should_tick2 += PLOT_W / y_ticks
        print("|", end="")
    else:
        print("-", end="")
print("  -> y", end="")


for step in range(n_steps):
    x = start + step * step_size
    if n_func == 1:
        y = x - 0.5 ** x
    else:
        y = x**3 - 4.49 * x ** 2 - 24.5 * x + 19.5




