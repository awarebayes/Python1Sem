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


size = 3
mat = [[i + j * size + 1 for i in range(size)] for j in range(size)]

r1 = rotate_cw(mat)
r2 = rotate_cw(r1)
r3 = rotate_cw(r2)

top = cat_horizontal(mat, r1)
bottom = cat_horizontal(r3, r2)
pprint_mat(cat_vertical(top, bottom))
