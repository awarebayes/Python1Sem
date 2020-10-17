x = float(input(">>> x (float): "))
eps = float(input(">>> epsilon (positive float): "))
max_iter = int(input(">>> max iter (positive int): "))

max_reached = False
x_n = 1
s = x_n
i = 1
counter = 0
while True:
    x_n *= x * x / (i * (i + 1))
    i += 2
    s += x_n
    if abs(x_n) < eps:
        break
    counter += 1
    if counter > max_iter:
        max_reached = True
        break

if max_reached:
    print("Max reached but x_n > epsilon")
else:
    print(f"End sum: {s:g}")
