from collections import defaultdict
import random
from math import ceil

def pprint_mat(m):
    for row in m:
        print(" ".join([f"{i:^3}" for i in row]))


def rotate_cw(m):
    out = [[0 for col in range(len(m))] for row in range(len(m))]
    outer_col = size - 1
    for row in m:
        for row_idx, row_i in enumerate(row):
            out[row_idx][outer_col] = row_i
        outer_col -= 1
    return out


def cat_horizontal(mat1, mat2):
    assert len(mat1) == len(mat2)
    out = []
    for row1 in range(len(mat1)):
        out.append(mat1[row1])

    for row2 in range(len(mat2)):
        out[row2].extend(mat2[row2])

    return out


def cat_vertical(mat1, mat2):
    assert len(mat1[0]) == len(mat2[0])
    w = len(mat1[0])
    h1 = len(mat1)
    h2 = len(mat2)
    out = [[0 for i in range(w)] for j in range(h1 + h2)]
    for row in range(h1):
        for col in range(w):
            out[row][col] = mat1[row][col]

    for row in range(h2):
        for col in range(w):
            out[row + h2][col] = mat2[row][col]
    return out

def get_quadriple_matrix(size):
    mat = [[i + j * size + 1 for i in range(size)] for j in range(size)]

    r1 = rotate_cw(mat)
    r2 = rotate_cw(r1)
    r3 = rotate_cw(r2)

    top = cat_horizontal(mat, r1)
    bottom = cat_horizontal(r3, r2)
    mat = cat_vertical(top, bottom)  
    return mat

# upper left: [row, col]
# upper right: [col][n-row-1]
# lower left: [n-1-row][n-col-1]
# lower right: [col][n-row-1]
def zero_unique_once(mat):
    h = len(mat)
    w = len(mat[0])
    for row in range(h//2):
        for col in range(w//2):
            choice = random.randint(0, 3)
            # upper left
            if choice == 0:
                mat[row][col] = 0
            # upper right
            elif choice == 1:
                mat[col][h-row-1] = 0
            # lower left
            elif choice == 2:
                mat[h-row-1][w-col-1] = 0
            # lower right
            elif choice == 3:
                mat[col][h-row-1] = 0 
    return mat


def gen_string_mat(size, from_mat, replacements):
    mat = [[''] * size * 2 for _ in range(2*size)]
    idx = 0
    for row in range(size*2):
        for col in range(size*2):
            if from_mat[row][col] == 0:
                if idx == len(replacements) - 1:                        
                    return
                mat[row][col] = replacements[idx]
                idx += 1
    return mat

def mat_to_string(mat):
    h = len(mat)
    w = len(mat[0])
    out = ""
    for row in range(h//2):
        for col in range(w//2):
            choice = random.randint(0, 3)
            # upper left
            if mat[row][col] != "":
                out += mat[row][col]
            # upper right
            elif mat[col][h-row-1] != "":
                out += mat[col][h-row-1]
            # lower left
            elif mat[h-row-1][w-col-1] != "":
                out += mat[h-row-1][w-col-1]
            # lower right
            elif mat[col][h-row-1] != "":
                out +=  mat[col][h-row-1]
    return out
 

input_str = "abcde"
size = ceil((len(input_str)/4)**0.5)

mat = get_quadriple_matrix(size)
mat = zero_unique_once(mat)
pprint_mat(mat)

str_mat = gen_string_mat(size, mat, input_str)

print("\n".join(["_".join([str(j) for j in i]) for i in str_mat]))
print(mat_to_string(str_mat))
