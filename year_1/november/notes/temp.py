cols = ["a", "1", "123123123123", "aaa"], ["12", "34", "45", "23"]
print(tuple(zip(*cols)))

"""
# 1. 
size = int(input(">>> size: "))
mat =  [[randint(0,100) for i in range(size)] for j in range(size)]
acc = 0

for row in range(size):
    for col in range(size):
        if col >= size-row-1 and col >= row:
            acc += mat[row][col]
        if col <= size-row-1 and col <= row:
            acc +=mat[row][col]

pprint_mat(mat)

print("sum: ", acc)
"""

# 2.
"""
h = 6 # width
w = 7 # height 
"
for row in range(h):
    for col in range(w):
        if col > symm * 2:
            mat[row][col] = 0
        elif col > symm:
            mat[row][col],  mat[row][symm*2-col] = mat[row][symm*2-col], mat[row][col] 

pprint_mat(mat)
"""
