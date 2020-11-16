# generate matrix of form
# 0 1  1  1 1
# 2 0  1  1 1
# 3 6  0  1 1
# 4 7  9  0 1
# 5 8 10 11 0
# Define array of means for each column
# Find max mean of columns
# Написал: Щербина МА ИУ7  15Б

from utils import fool_proof_int_input


def main():
    h = fool_proof_int_input(">>> input size: ")
    mat = [[0 for i in range(h)] for j in range(h)]
    # mat = [[0]*5]

    # generate matrix
    counter = 2
    for i in range(h):
        for j in range(h):
            if j > i:
                mat[i][j] = 1  # zero
            if i < j:
                mat[j][i] += counter  # some sequence
                counter += 1

    # pretty print matrix
    print("matrix")
    for i in mat:
        print(" ".join(map(lambda x: f"{str(x):^2}", i)))

    means = [0] * h  # means in columns

    # calculate mean
    for i in range(h):
        for j in range(h):
            means[i] += mat[j][i]  # sum of column
        means[i] /= h  # / no elemens

    print("means:")
    for idx, mean in enumerate(means):
        print("C", idx, f"mean {mean:g}")

    max_idx = 0  # max mean idx
    # find max idx
    for i in range(h):
        if means[max_idx] < means[i]:
            max_idx = i

    print(f"max mean is {means[max_idx]:g}", "is column", max_idx + 1)


if __name__ == "__main__":
    main()
