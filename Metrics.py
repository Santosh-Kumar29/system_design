# it is a simple 2d array
## it sotoring the numer into row and column

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

## get 5
matrix[1][1]


for rows in matrix:
    for column in rows:
        print(column)
        break


symbol = 1

matrix = [
    [1,2,3],
    [4,1,6],
    [7,8,1]
]


"""
[00, 01, 02]in
[10, 11, 12]
[20, 21, 22]

"""
for row in matrix:
    if row[0]  == row[1] == row[2] == symbol:
        print("matched")
        break
for col in range(3):
    if matrix[0][col] == matrix[1][col] == matrix[2][col] == symbol:
        print("matched")
        break

#left_diagonal = 
if matrix[0][0] == matrix[1][1] == matrix[2][2] == symbol:
    print("left diagonal match")
if matrix[0][2] == matrix[1][1] == matrix[2][2] == symbol:
    print("right diagonal")


