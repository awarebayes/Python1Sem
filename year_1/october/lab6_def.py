"""
>>> n - кол во вводимых далее чисел
>>> вводятся числа
вводится одно число m
вывести сколько раз введено ранее было введено m
"""

n = int(input(">>>> n numbers: "))
max_n = 100
mod_n = [0] * 100

for i in range(n):
    k = int(input(f">>> k[{i}] "))
    mod_n[k] += 1

k = int(input("final k query: "))
print(k, "has", mod_n[k], "occurrences")
