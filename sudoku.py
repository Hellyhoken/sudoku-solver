"""
#impossible
board = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
    ]

#expert
board = [
    [0,8,0,7,0,4,6,0,0],
    [1,0,0,0,0,0,0,0,8],
    [2,0,0,0,0,0,0,0,0],
    [7,0,0,0,1,0,4,0,0],
    [0,0,9,0,0,0,0,0,3],
    [6,1,0,0,0,2,9,0,0],
    [0,5,0,0,0,0,0,0,0],
    [0,6,0,5,0,0,1,0,4],
    [0,0,0,4,9,0,7,0,0]
    ]

#expert
board = [
    [0,0,0,0,7,0,1,0,0],
    [0,0,0,5,6,0,0,0,0],
    [0,8,0,0,2,0,0,3,0],
    [0,0,0,0,0,0,4,9,0],
    [0,4,0,2,5,0,0,0,8],
    [5,0,0,9,0,0,0,0,6],
    [4,0,6,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0],
    [7,0,0,1,9,0,8,0,0]]

#hard
board = [
    [0,0,0,8,0,0,4,2,0],
    [5,0,0,6,7,0,0,0,0],
    [0,0,0,0,0,9,0,0,5],
    [7,4,0,1,0,0,0,0,0],
    [0,0,9,0,3,0,7,0,0],
    [0,0,0,0,0,7,0,4,8],
    [8,0,0,4,0,0,0,0,0],
    [0,0,0,0,9,8,0,0,3],
    [0,9,5,0,0,3,0,0,0]
    ]

#medium
board = [
    [0,0,0,0,0,0,0,2,8],
    [0,6,0,0,0,0,0,0,7],
    [0,0,0,4,0,1,0,0,0],
    [5,0,0,9,7,0,3,0,0],
    [2,0,4,0,0,8,0,0,0],
    [3,0,0,0,0,4,5,0,0],
    [1,3,0,0,9,0,0,0,0],
    [0,5,7,0,0,0,0,9,0],
    [0,0,8,3,1,7,0,0,0]
    ]
"""

#impossible^2
board = [
    [0,0,0,1,0,2,0,0,0],
    [0,6,0,0,0,0,0,7,0],
    [0,0,8,0,0,0,9,0,0],
    [4,0,0,0,0,0,0,0,3],
    [0,5,0,0,0,7,0,0,0],
    [2,0,0,0,8,0,0,0,1],
    [0,0,3,0,0,0,8,0,5],
    [0,7,0,0,0,0,0,6,0],
    [0,0,0,3,0,4,0,0,0]
    ]






def make_possible_array(board):
    arr = []
    for i in range(9):
        l1 = []
        for j in range(9):
            l2 = []
            for l in range(9):
                if board[i][j] == 0:
                    l2.append(1)
                else:
                    l2.append(0)
            l1.append(l2)
        arr.append(l1)
    return arr

def print_board(board):
    for i in board:
        for j in i:
            if j == 0:
                print(" ", end = " ")
            else:
                print(j, end = " ")
        print("")

def print_possible(pos):
    for y in pos:
        for x in y:
            out = []
            for i in range(9):
                if x[i] != 0:
                    out.append(i+1)
            print(out,end=" ")
        print("")
def is_full(board):
    for i in board:
        for j in i:
            if j == 0:
                return False
    return True

def check_row(row):
    out = []
    for i in row:
        if i != 0:
            out.append(i)
    return out
        
def check_column(board, column):
    out = []
    for i in board:
        if i[column] != 0:
            out.append(i[column])
    return out

def check_box(board, x, y):
    out = []
    boxx = int((x - x % 3) / 3)
    boxy = int((y - y % 3) / 3)
    for i in range(3):
        for j in range(3):
            if board[boxy*3+i][boxx*3+j] != 0:
                out.append(board[boxy*3+i][boxx*3+j])
    return out

def check_pos_line(pos,board):
    for boxx in range(3):
        for boxy in range(3):
            for i in range(9):
                posposes = []
                filled = False
                for x in range(3):
                    for y in range(3):
                        if board[boxy*3+y][boxx*3+x] == i + 1:
                            filled = True
                            break
                        if pos[boxy*3+y][boxx*3+x][i] == 1:
                            posposes.append([x,y])
                    if filled:
                        break
                if len(posposes) != 0 and not filled:
                    rowlock = True
                    collock = True
                    row = posposes[0][1]
                    col = posposes[0][0]
                    if len(posposes) > 1:
                        for j in posposes[1:]:
                            if rowlock:
                                rowlock = (row == j[1])
                            if collock:
                                collock = (col == j[0])
                    if rowlock:
                        pos[boxy*3+row] = clear_pos_row(pos[boxy*3+row],boxx,i)
                    if collock:
                        pos = clear_pos_col(pos, boxx*3+col,boxy,i)
    return pos

def check_pos_box_line(board,pos):
    for row in range(9):
        for i in range(9):
            has = False
            posi = []
            for col in range(9):
                if board[row][col] == i + 1:
                    has = True
                    break
                if pos[row][col][i] == 1:
                    posi.append(col)
            if has:
                continue
            if len(posi) > 1:
                locked = True
                posboxx = int(posi[0]/3)
                for j in posi[1:]:
                    if locked:
                        locked = (posboxx == int(j/3))
                if locked:
                    sparerow = row % 3
                    boxy = int(row/3)
                    for y in range(3):
                        if y == sparerow:
                            continue
                        for x in range(3):
                            pos[boxy*3+y][posboxx*3+x][i] = 0
    
    for col in range(9):
        for i in range(9):
            has = False
            posi = []
            for row in range(9):
                if board[row][col] == i + 1:
                    has = True
                    break
                if pos[row][col][i] == 1:
                    posi.append(row)
            if has:
                continue
            if len(posi) > 1:
                locked = True
                posboxy = int(posi[0]/3)
                for j in posi[1:]:
                    if locked:
                        locked = (posboxy == int(j/3))
                if locked:
                    sparecol = col % 3
                    boxx = int(col/3)
                    for x in range(3):
                        if x == sparecol:
                            continue
                        for y in range(3):
                            pos[posboxy*3+y][boxx*3+x][i] = 0
    return pos
                

def clear_pos_row(row, skipbox, i):
    for j in range(9):
        if int(j/3) == skipbox:
            continue
        row[j][i] = 0
    return row

def clear_pos_col(pos, x, skipbox, i):
    for j in range(9):
        if int(j/3) == skipbox:
            continue
        pos[j][x][i] = 0
    return pos

def check_pos_row(row):
    out = [0,0,0,0,0,0,0,0,0]
    for i in row:
        for j in range(9):
            out[j] += i[j]
    return out
        
def check_pos_column(pos, column):
    out = [0,0,0,0,0,0,0,0,0]
    for i in pos:
        for j in range(9):
            out[j] += i[column][j]
    return out

def check_pos_box(pos, x, y):
    out = [0,0,0,0,0,0,0,0,0]
    boxx = int((x - x % 3) / 3)
    boxy = int((y - y % 3) / 3)
    for i in range(3):
        for j in range(3):
            for l in range(9):
                out[l] += pos[boxy*3+i][boxx*3+j][l]
    return out


def copy_pos(pos):
    out = []
    for i in pos:
        l1 = []
        for j in i:
            l2 = []
            for l in j:
                l2.append(l)
            l1.append(l2)
        out.append(l1)
    return out

def clone_board(board):
    out = []
    for i in board:
        l1 = []
        for j in i:
            l1.append(j)
        out.append(l1)
    return out

def find_low_pos(pos):
    i = 2
    out_val = []
    while i < 9:
        for j in range(9):
            for l in range(9):
                square = pos[j][l]
                if square.count(1) == i:
                    for k in range(9):
                        if square[k] == 1:
                            out_val.append(k + 1)
                    return {"value": out_val, "row": j, "col": l}
        i += 1
                        

def solve(board):
    testing = []
    testingpos = []
    if_failed = []
    pos = make_possible_array(board)
    while not is_full(board):
        prev = copy_pos(pos)
        for y in range(9):
            for x in range(9):
                if board[y][x] != 0:
                    continue
                for i in check_row(board[y]):
                    pos[y][x][i-1] = 0
                for i in check_column(board, x):
                    pos[y][x][i-1] = 0
                for i in check_box(board, x, y):
                    pos[y][x][i-1] = 0
                posrow = check_pos_row(pos[y])
                valcng = False
                for i in range(9):
                    if posrow[i] == 1 and pos[y][x][i] == 1:
                        board[y][x] = i + 1
                        print("put",i+1,"in",x+1,y+1,"by row")
                        pos[y][x] = [0,0,0,0,0,0,0,0,0]
                        valcng = True
                        break
                if valcng:
                    continue
                poscolumn = check_pos_column(pos, x)
                for i in range(9):
                    if poscolumn[i] == 1 and pos[y][x][i] == 1:
                        board[y][x] = i + 1
                        print("put",i+1,"in",x+1,y+1,"by column")
                        pos[y][x] = [0,0,0,0,0,0,0,0,0]
                        valcng = True
                        break
                if valcng:
                    continue
                posbox = check_pos_box(pos, x, y)
                for i in range(9):
                    if posbox[i] == 1 and pos[y][x][i] == 1:
                        board[y][x] = i + 1
                        print("put",i+1,"in",x+1,y+1,"by box")
                        pos[y][x] = [0,0,0,0,0,0,0,0,0]
                        valcng = True
                        break
                if valcng:
                    continue
                if pos[y][x].count(1) == 1:
                    board[y][x] = pos[y][x].index(1) + 1
                    print("put",pos[y][x].index(1) + 1,"in",x+1,y+1,"by elimination")
                    pos[y][x] = [0,0,0,0,0,0,0,0,0]
                elif pos[y][x].count(1) == 0:
                    done = False
                    while not done:
                        done = True
                        if len(if_failed[-1]["value"]) == 0:
                            testing.pop()
                            testingpos.pop()
                            if_failed.pop()
                            done = False
                    board = clone_board(testing[-1])
                    pos = copy_pos(testingpos[-1])
                    print("put",if_failed[-1]["value"][0],"in",if_failed[-1]["col"]+1,if_failed[-1]["row"]+1,"to test")
                    board[if_failed[-1]["row"]][if_failed[-1]["col"]] = if_failed[-1]["value"].pop(0)
                    pos[if_failed[-1]["row"]][if_failed[-1]["col"]] = [0,0,0,0,0,0,0,0,0]
                    
        pos = check_pos_line(pos,board)
        pos = check_pos_box_line(board,pos)
        if prev == pos:
            testing.append(clone_board(board))
            testingpos.append(copy_pos(pos))
            if_failed.append(find_low_pos(pos))
            print("put",if_failed[-1]["value"][0],"in",if_failed[-1]["col"]+1,if_failed[-1]["row"]+1,"to test")
            board[if_failed[-1]["row"]][if_failed[-1]["col"]] = if_failed[-1]["value"].pop(0)
            pos[if_failed[-1]["row"]][if_failed[-1]["col"]] = [0,0,0,0,0,0,0,0,0]
    return board

print_board(solve(board))
