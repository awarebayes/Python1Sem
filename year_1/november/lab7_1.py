# matrix
# 0 1  1  1 1
# 2 0  1  1 1
# 3 6  0  1 1
# 4 7  9  0 1
# 5 8 10 11 0
# Define [] mean of each column
# find max mean of columns
#  Написал: Щербина МА ИУ7  15Б

def main():
    mat = [[0 for i in range(5)] for j in range(5)]
    # mat = [[0]*5]*5

    # for i in mat:
    #    print(i)

    counter = 2
    for i in range(5):
        for j in range(5):
            if j > i:
                mat[i][j] = 1
            if i < j:
                mat[j][i] += counter
                counter += 1

    # pretty print matrix
    print("matrix")
    for i in mat:
        print(" ".join(map(lambda x: f"{str(x):^2}", i)))

    means = [0] * 5  # means in columns

    # calculate mean
    for i in range(5):
        for j in range(5):
            means[i] += mat[j][i] # sum of column
        means[i] /= 5 # / no elemens



    print("means:", means)

    max_idx = 0  # max mean idx
    # find max idx
    for i in range(5):
        if means[max_idx] < means[i]:
            max_idx = i

    print("max mean is", means[max_idx], "is column", max_idx + 1)

if __name__ == "__main__":
    main()