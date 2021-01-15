from util import *

# st = input("Ввод: ")
st = "abcde"

size = (len(st) / 4) ** 0.5
if size % 1 != 0:
    size = int(size) + 1
else:
    size = int(size)
print(size)

key_mat = gen_rotation_matrix(size)
key_mat = random_zero_matrix(key_mat)
dump_bin_mask(key_mat, "mask.txt")
encrypted = encrypt(key_mat, st)
dump_mat(encrypted, "encrypted.txt")

print("encrypted!")
