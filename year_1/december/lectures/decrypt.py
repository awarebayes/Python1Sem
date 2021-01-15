from .util import *

encrypted = read_mat("encrypted.txt")
bin_mask = read_bin_mask("mask.txt")
s = decrypt(bin_mask, encrypted)
print("decrypted:", s)
