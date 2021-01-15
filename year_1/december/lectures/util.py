import random


def square_zeros(size):
    return [[0] * (size) for i in range(size)]


def count_matrix(size):
    A = square_zeros(size)
    k = 1
    for i in range(size):
        for j in range(size):
            A[i][j] = k
            k += 1
    return A


def print_mat(mat):
    for row in mat:
        for elem in row:
            print("{0:^5.5g}".format(elem), end=" ")
        print()


def rotate(mat):
    mat.reverse()
    size = len(mat)
    for i in range(size):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


def gen_rotation_matrix(size):
    count_mat = count_matrix(size)
    key_mat = square_zeros(size * 2)
    for i in range(size):
        for j in range(size):
            key_mat[i][j] = count_mat[i][j]
    rotate(count_mat)

    for i in range(size):
        for j in range(size, size * 2):
            key_mat[i][j] = count_mat[i][j - size]
    rotate(count_mat)

    for i in range(size, size * 2):
        for j in range(size, size * 2):
            key_mat[i][j] = count_mat[i - size][j - size]
    rotate(count_mat)

    for i in range(size, size * 2):
        for j in range(size):
            key_mat[i][j] = count_mat[i - size][j]
    return key_mat


def random_zero_matrix(key_mat):
    size = len(key_mat) // 2
    # исходная матрица [i][j]
    # правый верхний угол [j][n-i-1]
    # левый нижний угол [n-1-i][n-1-j]
    # правый нижний угол [n-1-j][i]
    for i in range(size):
        for j in range(size):
            choice = random.randint(0, 3)
            if choice == 0:
                key_mat[i][j] = 0
            # правый верхний угол
            elif choice == 1:
                key_mat[j][size * 2 - 1 - i] = 0
            # левый нижний угол
            elif choice == 2:
                key_mat[size * 2 - 1 - i][size * 2 - 1 - j] = 0
            # правый нижний угол
            elif choice == 3:
                key_mat[size * 2 - 1 - j][i] = 0
    return key_mat


def dump_bin_mask(mat, filename):
    f = open(filename, "w", encoding="utf-8")
    for elem in mat:
        ans = ""
        for char in elem:
            if char == 0:
                ans += "1"
            else:
                ans += "0"
        f.write(str(int(ans, 2)) + "\n")
    f.close()


def encrypt(key_mat, to_encrypt):
    size = len(key_mat) // 2
    ind = 0
    encrypted = [["*"] * size * 2 for _ in range(2 * size)]
    for _ in range(4):
        for i in range(size * 2):
            for j in range(size * 2):
                if key_mat[i][j] == 0:
                    if ind == len(to_encrypt):
                        break
                    encrypted[i][j] = to_encrypt[ind]
                    ind += 1
            if ind == len(to_encrypt):
                break
        if ind == len(to_encrypt):
            break
        rotate(key_mat)
    return encrypted


def read_bin_mask(filename):
    f = open(filename, "r", encoding="utf-8")
    n_rows = 0
    for line in f:
        n_rows += 1
    f.close()

    bin_mask = square_zeros(n_rows)
    cur_row = 0

    f = open(filename, "r", encoding="utf-8")
    for line in f:
        number = bin(int(line))[2:]
        i = n_rows - 1
        for ch in number[::-1]:
            bin_mask[cur_row][i] = int(ch)
            i -= 1
        cur_row += 1
    f.close()
    return bin_mask


def decrypt(bin_mask, encrypted):
    k = len(bin_mask)
    out = ""
    flag = False

    for _ in range(4):
        for i in range(k):
            for j in range(k):
                if bin_mask[i][j] == 1 and len(encrypted[i][j]) > 0:
                    out += encrypted[i][j]
                elif bin_mask[i][j] == 1 and len(encrypted[i][j]) == 0:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
        rotate(bin_mask)
    return out


def dump_mat(mat, f_path):
    f = open(f_path, "w")
    for row in mat:
        for el in row:
            f.write(f"{el} ")
        f.write("\n")
    f.close()


def read_mat(f_path):
    f = open(f_path, "r")
    out = []
    for line in f:
        row = line.strip().split()
        row_temp = []
        for el in row:
            if el != "*":
                row_temp.append(el)
            else:
                row_temp.append("")
        out.append(row_temp)
    return out
