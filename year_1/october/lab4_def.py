# y = ln(x) * sin(a * x)
# >> a , x

from math import log, sin, inf

start = float(input(">>> x start (float):"))
end = float(input(">>> x end (float):"))
step = float(input(">>> step (float):"))
a = float(input(">>> a (float, parameter):"))

assert end > start
n_steps = int((end - start) // step)

f_min = inf
f_max = -inf
for i in range(n_steps + 1):
    x = start + i * step
    if x > end:
        break
    if x <= 0:
        continue
    f = log(x) * sin(a * x)
    f_min = min(f, f_min)
    f_max = max(f, f_max)
print(
    """
       _       _   
 _ __ | | ___ | |_ 
| '_ \| |/ _ \| __|
| |_) | | (_) | |_ 
| .__/|_|\___/ \__|
|_|   
___________________
"""
)


PLOT_W = 80
for i in range(n_steps + 1):
    x = start + i * step
    if x <= 0:
        print()
        continue
    f = log(x) * sin(a * x)
    y_norm = (f - f_min) / (f_max - f_min)
    assert 0 <= y_norm <= 1
    y_pos = int(PLOT_W * y_norm)
    print(" " * (y_pos) + "*")
