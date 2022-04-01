#It is a basic Tic Tac Toc game that is played on the console/terminal.
#Konsolda oynanan basit bir XOX oyunu

#There are probably better and more effective ways to implement this but this was a starting project of mine.
#Daha iyi ve etkili şekilde yapılabilir fakat başlangıç projelerimden biri olduğu için göz ardı edilebilir.




import numpy as np



def drawboard(size, matrix):
    """Tahta Çizmek için kullanılan fonksiyon,
        'size' is the size of the square board
        'matrix' is the matrix that will write into the board""" 
    
    board = ""
    cnt = 0

    for i in range(2*size + 1):

        if i%2 == 0:
            for j in range(size):
                board += " ---"
        
        elif i%2 != 0:
            for j in range(size + 1):
                if j == 0:
                    board += "|"
                else:
                    board += " " + str(matrix[cnt][j-1]) + "  |"
            cnt += 1

        board += "\n"
    
    return board



def check_win(matrix):
    """CheckWin system that checks if any player has won"""


#horizontal check
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] and matrix[i][0] != 0 :
            return matrix[i][0]

#vertical check
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] and matrix[0][i] != 0 :
            return matrix[0][i]

#diagonal check
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != 0 :
        return matrix[0][0]

    if matrix[2][0] == matrix[1][1] == matrix[0][2] and matrix[1][1] != 0 :
        return matrix[1][1]

#draw check
    if matrix[0][1] != 0 and matrix[0][1] != 0 and matrix[0][2] != 0 and matrix[1][0] != 0 and matrix[1][1] != 0 and matrix[1][2] != 0 and matrix[2][0] != 0 and matrix[2][1] != 0 and matrix[2][2] != 0 :
        return "draw"



check = True
turn = 0

grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

while check:
    if turn%2 == 0:
        move = str(input("Player 1 (X), put coordinates. row, column : "))
        x, y = move.split(",")
        x = int(x)
        y = int(y)
        assert grid[x-1][y-1] == 0, "Wrong move"

        grid[x-1][y-1] = "X"
        
        print(drawboard(3, grid))

        if check_win(grid) == "X":
            print("Player 1 has won")
            break

        if check_win(grid) == "draw":
            print("IT'S A DRAW")
            break
        
        turn += 1

    elif turn%2 != 0:
        move = str(input("Player 2 (O), put coordinates. row, column : "))
        x, y = move.split(",")
        x = int(x)
        y = int(y)

        assert grid[x-1][y-1] == 0, "Wrong move"

        grid[x-1][y-1] = "O"

        print(drawboard(3, grid))

        if check_win(grid) == "O":
            print("Player 2 has won")
            break

        if check_win(grid) == "draw":
            print("IT'S A DRAW")
            break

        turn += 1


