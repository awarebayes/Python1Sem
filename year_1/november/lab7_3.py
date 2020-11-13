# Написал: Щербина МА ИУ7  15Б
# given a matrix
# find the column with maximum number of zeros
# move it to the end of matrix
from utils import fool_proof_float_input

def pprint_mat(m):
    for i in m:
        print(" ".join(map(lambda x: f"{x:^12g}", i)))

def main():
    h = int(input(">>> n rows (int): " )) # height
    w = int(input(">>> n cols (int): " )) # width

    m = [[0 for i in range(w)] for j in range(h)] # matrix

    """
    for row in range(h):
        for col in range(w):
            m[row][col] = fool_proof_float_input(f"M[{row}, {col}] = ")
    """
    
    from random import uniform
    for row in range(h):
        for col in range(w):
            should_zero = uniform(0, 1)
            if should_zero > uniform(0.1, 0.7):
                m[row][col] = uniform(0,1)
            else:
                m[row][col] = 0

    print("\nBefore:")
    pprint_mat(m)

    n_zeros_col = [0 for i in range(w)] # number of zeros in column
    for col in range(w):
        for row in range(h):
            if m[row][col] == 0:
                n_zeros_col[col] += 1 # element in col is a zero


    # check whether any zeros:
    has_zero = False
    for col in n_zeros_col:
        if col > 0:
            has_zero = True

    if not has_zero:
        print("No zeros found")
        exit()

    # find an index of a column with most zeroes
    most_zeros_col = 0
    for col in range(w):
        if n_zeros_col[col] > n_zeros_col[most_zeros_col]:
            most_zeros_col = col

    print("\nColumn with most zeroes:", most_zeros_col)

    # move the column with most zeros to the end
    for row in range(h):
        m[row].append(m[row].pop(most_zeros_col))

    print("\nAfter:")
    pprint_mat(m)


if __name__ == "__main__":
    main()