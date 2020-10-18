import pyautogui as pg    
import numpy as np  
import time

#Im putting this here temporarily to backtrack to this point when i mess up and run the code on itself which just happens like every third time if my cursor is up here

grid = []

while True:
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        break
    print('Row'+str(len(grid)) + 'Complete')

time.sleep(1)


def possible(x,y,n):
    for i in range(0,9):
        if grid[i][x] == n:
            return False

    for i in range(0,9):
        if grid[y][i] == n:
            return False
    
    #This checks the box
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for x in range(x0, x0 + 3):
        for y in range(y0, y0 + 3):
            if grid[y][x] == n: 
                return False
        
    return True

def Print(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])
        
    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(x,y,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    Print(grid)
    input('More?')

solve()
Print(grid)

