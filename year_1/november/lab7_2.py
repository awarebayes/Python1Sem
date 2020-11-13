
# Написал: Щербина МА ИУ7  15Б
# find means of columns
# find n of elements less that mean in column


from math import exp
from random import uniform
from utils import fool_proof_float_input, fool_proof_int_input
S_LEN = 103 # length of formatted matrix string

# g = [uniform(1,4) for _ in range(8)]
# a = [uniform(1, 3) for _ in range(8)]

print('input two arrays')

len_g = fool_proof_int_input(">>> len of g: ")
len_a = fool_proof_int_input(">>> len of a: ")

g = [0] * len_g
a = [0] * len_a
for i in range(len_g):
    g[i] = fool_proof_float_input(f">>> g[{i}] = ")

print()
for i in range(len_a):
    a[i] = fool_proof_float_input(f">>> a[{i}] = ")


b = [[exp(i * k) for k in a] for i in g]


# pretty print matrix
print(f"\n{'MATRIX':^103}\n")
for i in b:
    print(" ".join(map(lambda x: f"{x:^12g}", i)))


means = [0] * len_a  # means in columns
# means is MN

# calculate mean
for i in range(len_a):
    for j in range(len_g):
        means[i] += b[j][i] # sum of column
    means[i] /= 8 # / no elemens

print(f"\n{'MEANS':^103}\n")

print(" ".join(map(lambda x: f"{x:^12g}", means)))

less_than_mean = [0] * len_a
# less than means is R

# calculate mean
for i in range(len_g):
    for j in range(len_a):
        if means[j] > b[i][j]:
            less_than_mean[j] += 1

print(" ".join(map(lambda x: f"{x:^12g}", less_than_mean)))