def bingo():
    boards_having_bingo = []
    with open("day4.in.txt") as input:
        bingo = [line.strip() for line in input if line != '']
    drawn_balls = [int(ball) for ball in bingo[0].split(',')]
    print(drawn_balls)
    boards = []
    current_board = []
    for i in range(2, len(bingo)+1):
        if(len(current_board) == 5):
            boards.append(current_board)
            current_board = []
        else:
            current_board.append([int(number) for number in bingo[i].split(' ') if number != '' ])
    for ball in drawn_balls: 
        print('drawing ball: '+str(ball))       
        for board in [b for b in boards if b not in boards_having_bingo]:
            for row in range(0, len(board)):
                for col in range(0, len(board)):
                    if board[row][col] == ball:
                        board[row][col] = -1
            print(board)
            print('')

            if checkboard(board) :
                print(board)
                sum_of_cells = 0
                for row in board:
                    for cell in row:
                        if cell > -1:
                            sum_of_cells += cell
                            
                print(sum_of_cells)
                print(ball)
                print(sum_of_cells * ball)
                boards_having_bingo.append(board)


def checkboard(board):
    r = False
    c = False
    for row in range(0, len(board)):
        row_has_bingo = True
        for col in range(0, len(board)):
            if board[row][col] != -1:
                row_has_bingo = False
                break

        if row_has_bingo:
            print("bingo in row: "+str(row))
            r = row_has_bingo

    for col in range(0, len(board)):
        col_has_bingo = True
        for row in range(0, len(board)):
            if board[row][col] != -1:
                col_has_bingo = False
                break
        if col_has_bingo:
            print("bingo in column "+str(col))
            c = col_has_bingo
    
    if r or c:
        print("BINGO")
        return True
                
bingo()