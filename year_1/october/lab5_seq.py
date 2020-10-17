#  Вычислить сумму ряда с заданой точностью
#  и вывести таблицу промежуточных значений

#  Написал: Щербина МА ИУ7  15Б

# McLauren's sequence
# sin x = x - x^3/3 + x^5/5 - x^7/7 + ...


x = float(input(">>> x (float): "))
eps = float(input(">>> epsilon (float): "))
log_step = int(input(">>> step in table (int): "))
max_iter = int(input(">>> max iter (int): "))


x_n = x  # nth term
s = x_n  # end sum
max_reached = False  # whether we reached max interation

if abs(x) < eps:
    print(f"End sum: {s:g}")
    exit(0)

# print table head
print("_" * (15 * 3 + 4))
print(f"|{'step':^15}|{'x_n':^15}|{'sum':^15}|")
print("-" * (15 * 3 + 4))

i = 3  # factorial iterator
step = 0  # while loop iterator
while True:
    # calculate n th term
    x_n *= -1 * x * x / i
    i += 2

    # check if still in boundaries
    if step >= max_iter:
        max_reached = True
        break
    if abs(x_n) < eps:
        break  # we are there at last

    # update loop variable and sum
    s += x_n
    step += 1
    if step % log_step == 0:
        print(f"|{step:^15}|{x_n:^15g}|{s:^15g}|")

print("⎻" * (15 * 3 + 4))

if max_reached:
    print("Max iteration reached but the sequence didn't converge!")
else:
    print(f"End sum: {s:g}")
