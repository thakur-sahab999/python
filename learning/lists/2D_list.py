num_grid = [
    [1,2,3],
    [5,6,7],
    [4,8,9],
    [0]
]

#number_grid[row no.][col no.]

print(num_grid[2][0])

#nested for loop
for rows in num_grid:
    for cols in rows:
        print(cols)