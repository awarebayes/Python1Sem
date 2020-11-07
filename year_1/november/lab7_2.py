
# Написал: Щербина МА ИУ7  15Б
# find means of columns
# find n of elements less that mean in column


from math import exp
from random import randint, uniform
S_LEN = 103 # length of formatted matrix string

#g = [uniform(1,4) for _ in range(8)]
#a = [randint(1, 3) for _ in range(8)]

print('input two arrays [8]')

g = [0] * 8
a = [0] * 8
for i in range(8):
    g[i] = float(input(f">>> g[{i}] = "))

print()
for i in range(8):
    a[i] = float(input(f">>> a[{i}] = "))


b = [[exp(i * k) for k in a] for i in g]


# pretty print matrix
print(f"\n{'MATRIX':^103}\n")
for i in b:
    print(" ".join(map(lambda x: f"{x:^12g}", i)))


means = [0] * 8  # means in columns
# means is MN

# calculate mean
for i in range(8):
    for j in range(8):
        means[i] += b[j][i] # sum of column
    means[i] /= 8 # / no elemens

print(f"\n{'MEANS':^103}\n")

print(" ".join(map(lambda x: f"{x:^12g}", means)))

less_than_mean = [0] * 8
# less than means is R

# calculate mean
for i in range(8):
    for j in range(8):
        if means[j] > b[i][j]:
            less_than_mean[j] += 1

print(" ".join(map(lambda x: f"{x:^12g}", less_than_mean)))