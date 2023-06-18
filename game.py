m=9
n=9
def puzzle(a):
    for i in range(m):
        for j in range(m):
            print(a[i][j],end=" ")
        print()
def sudoku(grid,row,col):
    if row==m-1 and col==m:
        return True
    if col==m:
        row+=1
        col=0
    if grid[row][col]>0:
        return sudoku(grid,row,col+1)
    for num in range(1,m+1,1):
        if solve(grid,row,col,num):
            grid[row][col]=num
            if sudoku(grid,row,col+1):
                return True
        grid[row][col]=0
    return False
def solve(grid,row,col,num):
    for x in range(m):
        if grid[row][x]==num:
            return False
    for x in range(m):
        if grid[x][col]==num:
            return False
    startRow=row-row%3
    startCol=col-col%3
    for i in range(3):
        for j in range(3):
            if grid[i+startRow][j+startCol]==num:
                return False
    return True
grid=[[2, 5, 0, 0, 3, 0, 9, 0, 1],
      [0, 1, 0, 0, 0, 4, 0, 0, 0],
      [4, 0, 7, 0, 0, 0, 2, 0, 8],
      [0, 0, 5, 2, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 9, 8, 1, 0, 0],
      [0, 4, 0, 0, 0, 3, 0, 0, 0],
      [0, 0, 0, 3, 6, 0, 0, 7, 2],
      [0, 7, 0, 0, 0, 0, 0, 0, 3],
      [9, 0, 3, 0, 0, 0, 6, 0, 4]]

if (sudoku(grid,0,0)):
   puzzle(grid)
else:
    print("no solution")
