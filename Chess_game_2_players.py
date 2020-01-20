from tkinter import *

# creating the parameters (each square of te chessboard will be stocked in a dictionnary)

turn='white'
Board_dict={}
dep_square=(-1,-1)
my_font = "{courier new} 50"
my_font_2 = "{courier new} 20"

# creating the chessboard

def N_empty_lines(n):
    return [Empty_line_of_n(8) for i in range(n)]

def Empty_line_of_n(n):
    return [[' ',' '] for i in range(n)]

Pieces_line=['T','C','F','D','R','F','C','T']

White_pieces_line=[[name,'white'] for name in Pieces_line]

Black_pieces_line=[[name,'black'] for name in Pieces_line]

White_pawns_line=[['P','white'] for i in range(8)]

Black_pawns_line=[['P','black'] for i in range(8)]

dep_chessboard=[Black_pieces_line, Black_pawns_line] + N_empty_lines(4) + [White_pawns_line, White_pieces_line]

Chessboard=dep_chessboard


# function returning all the possible moves of a piece based on the type of piece (including moves that would bring to a self-check)

def Piece_moves(Chessboard, dep_pos):
    lin=dep_pos[0]
    col=dep_pos[1]
    piece_type=Chessboard[lin][col][0]
    if piece_type=='P':
        return Pawn_moves(Chessboard, dep_pos)
    elif piece_type=='T':
        return Rook_moves(Chessboard, dep_pos)
    elif piece_type=='F':
        return Bishop_moves(Chessboard, dep_pos)
    elif piece_type=='C':
        return Knight_moves(Chessboard, dep_pos)
    elif piece_type=='R':
        return King_moves(Chessboard, dep_pos)
    elif piece_type=='D':
        return Queen_moves(Chessboard, dep_pos)

# function returning all the possible moves of a pawn(a case-disjunction based on the color is needed )

def Pawn_moves(Chessboard, dep_pos):
    possible_moves=[]
    lin=dep_pos[0]
    col=dep_pos[1]
    if Chessboard[lin][col][1]=='white':
        if lin>0:
            if Chessboard[lin-1][col]==[' ',' ']:
                if lin==6 and Chessboard[lin-2][col]==[' ',' ']:
                    possible_moves.append((lin-2,col))
                possible_moves.append((lin-1,col))
            if (col>0) and Chessboard[lin-1][col-1][1]=='black':
                    possible_moves.append((lin-1,col-1))
            if (col<7) and Chessboard[lin-1][col+1][1]=='black':
                    possible_moves.append((lin-1,col+1))
    else:
        if lin<7:
            if Chessboard[lin+1][col]==[' ',' ']:
                if lin==1 and Chessboard[lin+2][col]==[' ',' ']:
                    possible_moves.append((lin+2,col))
                possible_moves.append((lin+1,col))
            if (col>0) and Chessboard[lin+1][col-1][1]=='white':
                possible_moves.append((lin+1,col+1))
            if (col<7) and Chessboard[lin+1][col+1][1]=='white':
                possible_moves.append((lin+1,col+1))
    return possible_moves

# function returning all the possible moves of a rook

def Rook_moves(Chessboard, dep_pos):
    possible_moves=[]
    lin=dep_pos[0]
    col=dep_pos[1]
    lin_minus=lin
    while lin_minus>0 and Chessboard[lin_minus-1][col][1]==' ':
        possible_moves.append((lin_minus-1,col))
        lin_minus=lin_minus-1
    if lin_minus>0 and Chessboard[lin_minus-1][col][1]!=Chessboard[lin][col][1]:
        possible_moves.append((lin_minus-1,col))
    lin_plus=lin
    while lin_plus<7 and Chessboard[lin_plus+1][col][1]==' ':
        possible_moves.append((lin_plus+1,col))
        lin_plus=lin_plus+1
    if lin_plus>0 and Chessboard[lin_plus-1][col][1]!=Chessboard[lin][col][1]:
        possible_moves.append((lin_plus-1,col))
    col_minus=col
    while col_minus>0 and Chessboard[lin][col_minus-1][1]==' ':
        possible_moves.append((lin,col_minus-1))
        col_minus=col_minus-1
    if col_minus>0 and Chessboard[lin][col_minus-1][1]!=Chessboard[lin][col][1]:
        possible_moves.append((lin,col_minus-1))
    col_plus=col
    while col_plus<7 and Chessboard[lin][col_plus+1][1]==' ':
        possible_moves.append((lin,col_plus+1))
        col_plus=col_plus+1
    if col_plus<7 and Chessboard[lin][col_plus+1][1]!=Chessboard[lin][col][1]:
        possible_moves.append((lin,col_plus+1))
    return possible_moves

# function returning all the possible moves of a bishop

def Bishop_moves(Chessboard, dep_pos):
    possible_moves=[]
    lin=dep_pos[0]
    col=dep_pos[1]
    lin_NW=lin
    col_NW=col
    while lin_NW>0 and col_NW>0 and Chessboard[lin_NW-1][col_NW-1][1]==' ':
        possible_moves.append((lin_NW-1,col_NW-1))
        lin_NW=lin_NW-1
        col_NW=col_NW-1
    if lin_NW>0 and col_NW>0 and Chessboard[lin_NW-1][col_NW-1][1]!=Chessboard[lin][col][1]:
        possible_moves.append((lin_NW-1,col_NW-1))
    lin_NE=lin
    col_NE=col
    while lin_NE>0 and col_NE<7 and Chessboard[lin_NE-1][col_NE+1][1]==' ':
        possible_moves.append((lin_NE-1,col_NE+1))
        lin_NE=lin_NE-1
        col_NE=col_NE+1
    if lin_NE>0 and col_NE<7 and Chessboard[lin_NE-1][col_NE+1][1]!=Chessboard[lin][col][1]:
        possible_moves.append((lin_NE-1,col_NE+1))
    lin_SE=lin
    col_SE=col
    while lin_SE<7 and col_SE<7 and Chessboard[lin_SE+1][col_SE+1][1]==' ':
        possible_moves.append((lin_SE+1,col_SE+1))
        lin_SE=lin_SE+1
        col_SE=col_SE+1
    if lin_SE<7 and col_SE<7 and Chessboard[lin_SE+1][col_SE+1][1]!=Chessboard[lin][col][1]:
        possible_moves.append((lin_SE+1,col_SE+1))
    lin_SW=lin
    col_SW=col
    while lin_SW<7 and col_SW>0 and Chessboard[lin_SW+1][col_SW-1][1]==' ':
        possible_moves.append((lin_SW+1,col_SW-1))
        lin_SW=lin_SW+1
        col_SW=col_SW-1
    if lin_SW<7 and col_SW>0 and Chessboard[lin_SW+1][col_SW-1][1]!=Chessboard[lin][col][1]:
        possible_moves.append((lin_SW+1,col_SW-1))
    return possible_moves

# function returning all the possible moves of a queen

def Queen_moves(Chessboard, dep_pos):
    Mouvs_dame=Bishop_moves(Chessboard, dep_pos)
    Mouvs_dame.extend(pos for pos in Rook_moves(Chessboard, dep_pos) if not pos in Mouvs_dame)
    return Bishop_moves(Chessboard, dep_pos) + Rook_moves(Chessboard, dep_pos)

# function returning all the possible moves of a knight

Knight_all_moves=[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

def Knight_moves(Chessboard, dep_pos):
    possible_moves=[]
    lin=dep_pos[0]
    col=dep_pos[1]
    for mov in Knight_all_moves:
        if lin+mov[0]>-1 and lin+mov[0]<8 and col+mov[1]>-1 and col+mov[1]<8 and Chessboard[lin+mov[0]][col+mov[1]][1]!=Chessboard[lin][col][1]:
            possible_moves.append((lin+mov[0],col+mov[1]))
    return possible_moves

# function returning all the possible moves of a king

King_all_moves=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def King_moves(Chessboard, dep_pos):
    possible_moves=[]
    lin=dep_pos[0]
    col=dep_pos[1]
    for mov in King_all_moves:
        arr_lin=lin+mov[0]
        arr_col=col+mov[1]
        if arr_lin<8 and arr_lin>-1 and arr_col<8 and arr_col>-1 and Chessboard[arr_lin][arr_col][1]!=Chessboard[lin][col][1]:
            possible_moves.append((arr_lin,arr_col))
    return possible_moves

# function returning if the player puts himself in check as first argument, and if the second player is in check as second argument

def check(chessboard, turn):
    self_check=False
    VS_check=False
    for i in range(8):
        for j in range(8):
            test_square=chessboard[i][j]
            if not test_square[0]==' ':
                if test_square[0]=='T':
                    for arr_pos in Rook_moves(chessboard, (i,j)):
                        arr_square=chessboard[arr_pos[0]][arr_pos[1]]
                        if arr_square[0]=='R' and arr_square[1]!=test_square[1]:
                            if arr_square[1]==turn:
                                self_check=True
                            else:
                                VS_check=True
                elif test_square[0]=='C':
                    for arr_pos in Knight_moves(chessboard, (i,j)):
                        arr_square=chessboard[arr_pos[0]][arr_pos[1]]
                        if arr_square[0]=='R' and arr_square[1]!=test_square[1]:
                            if arr_square[1]==turn:
                                self_check=True
                            else:
                                VS_check=True
                elif test_square[0]=='F':
                    for arr_pos in Bishop_moves(chessboard, (i,j)):
                        arr_square=chessboard[arr_pos[0]][arr_pos[1]]
                        if arr_square[0]=='R' and arr_square[1]!=test_square[1]:
                            if arr_square[1]==turn:
                                self_check=True
                            else:
                                VS_check=True
                elif test_square[0]=='D':
                    for arr_pos in Queen_moves(chessboard, (i,j)):
                        arr_square=chessboard[arr_pos[0]][arr_pos[1]]
                        if arr_square[0]=='R' and arr_square[1]!=test_square[1]:
                            if arr_square[1]==turn:
                                self_check=True
                            else:
                                VS_check=True
                elif test_square[0]=='P':
                    if test_square[1]=='white':
                        if i>0 and j>0 and chessboard[i-1][j-1][0]=='R' and chessboard[i-1][j-1][1]!=test_square[1]:
                            if test_square[1]!=turn:
                                self_check=True
                            else:
                                VS_check=True
                        elif i>0 and j<7 and chessboard[i-1][j+1][0]=='R' and chessboard[i-1][j+1][1]!=test_square[1]:
                            if test_square[1]!=turn:
                                self_check=True
                            else:
                                VS_check=True
                    else:
                        if i<7 and j>0 and chessboard[i+1][j-1][0]=='R' and chessboard[i+1][j-1][1]!=test_square[1]:
                            if test_square[1]!=turn:
                                self_check=True
                            else:
                                VS_check=True
                        elif i<7 and j<7 and chessboard[i+1][j+1][0]=='R' and chessboard[i+1][j+1][1]!=test_square[1]:
                            if test_square[1]!=turn:
                                self_check=True
                            else:
                                VS_check=True

    return (self_check, VS_check)

# function returning if the second player is checkmated

def checkmate(chessboard, turn):
    mate=True
    if turn=='white':
        turn='black'
        for k in range(8):
            for l in range(8):
                test_square_mate=chessboard[k][l]
                if test_square_mate[1]==turn:
                    for mouvs in Piece_moves(chessboard, (k,l)):
                        arr_square_test_mate=chessboard[mouvs[0]][mouvs[1]]
                        chessboard[mouvs[0]][mouvs[1]]=test_square_mate
                        chessboard[k][l]=[' ',' ']
                        if not check(chessboard, turn)[0]:
                            mate=False
                            chessboard[k][l]=chessboard[mouvs[0]][mouvs[1]]
                            chessboard[mouvs[0]][mouvs[1]]=arr_square_test_mate
                            break
                        chessboard[k][l]=chessboard[mouvs[0]][mouvs[1]]
                        chessboard[mouvs[0]][mouvs[1]]=arr_square_test_mate
                    else:
                        continue
                    break
            else:
                continue
            break
    else:
        turn='white'
        for k in range(8):
            for l in range(8):
                test_square_mate=chessboard[k][l]
                if test_square_mate[1]==turn:
                    for mouvs in Piece_moves(chessboard, (k,l)):
                        arr_square_test_mate=chessboard[mouvs[0]][mouvs[1]]
                        chessboard[mouvs[0]][mouvs[1]]=test_square_mate
                        chessboard[k][l]=[' ',' ']
                        if not check(chessboard, turn)[0]:
                            mate=False
                            chessboard[k][l]=chessboard[mouvs[0]][mouvs[1]]
                            chessboard[mouvs[0]][mouvs[1]]=arr_square_test_mate
                            break
                        chessboard[k][l]=chessboard[mouvs[0]][mouvs[1]]
                        chessboard[mouvs[0]][mouvs[1]]=arr_square_test_mate
                    else:
                        continue
                    break
            else:
                continue
            break
    if turn=='black':
        turn='white'
    else:
        turn='black'
    return mate

# function moving the pieces on the chessboard : players must click on a piece to move then click on the square they want to move it (if the square is not a possible move, player must re-click on the piece)

def Move(lin, col):
    global dep_square, turn, fenetre
    if dep_square[0]<0:
        if Chessboard[lin][col][1]==turn:
            dep_square=(lin,col)
    elif (lin,col) in Piece_moves(Chessboard, dep_square):
        squarearrprov=Chessboard[lin][col]
        squaredepprov=Chessboard[dep_square[0]][dep_square[1]]
        Chessboard[lin][col]=Chessboard[dep_square[0]][dep_square[1]]
        Chessboard[dep_square[0]][dep_square[1]]=[' ',' ']
        if check(Chessboard, turn)[0]:
            Chessboard[lin][col]=squarearrprov
            Chessboard[dep_square[0]][dep_square[1]]=squaredepprov
            dep_square=(-1,-1)
        else:
            image_square_color(lin, col)
            Board_dict[(dep_square[0],dep_square[1])].configure(text='')
            dep_square=(-1,-1)
            if check(Chessboard, turn)[1]:
                if checkmate(Chessboard, turn):
                    Escape.configure(text='%s player won. Quit' % turn)
                    Escape.place(x=100, y=600)
            if turn=='white':
                turn='black'
            else:
                turn='white'
            Indicate_turn.configure(text='%s player turn' % turn)
    else:
        dep_square=(-1,-1)

def image_square_color(i, j):
    color_piece=Chessboard[i][j][1]
    if color_piece=='white':
        image_white_square(i, j)
    else:
        image_black_square(i, j)

def image_white_square(i, j):
    piece_type=Chessboard[i][j][0]
    if piece_type=='P':
        Board_dict[(i, j)].configure(text=u'\u2659')
    elif piece_type=='T':
        Board_dict[(i, j)].configure(text=u'\u2656')
    elif piece_type=='F':
        Board_dict[(i, j)].configure(text=u'\u2657')
    elif piece_type=='C':
        Board_dict[(i, j)].configure(text=u'\u2658')
    elif piece_type=='R':
        Board_dict[(i, j)].configure(text=u'\u2654')

    elif piece_type=='D':
        Board_dict[(i, j)].configure(text=u'\u2655')

def image_black_square(i, j):
    piece_type=Chessboard[i][j][0]
    if piece_type=='P':
        Board_dict[(i, j)].configure(text=u'\u265F')
    elif piece_type=='T':
        Board_dict[(i, j)].configure(text=u'\u265C')
    elif piece_type=='F':
        Board_dict[(i, j)].configure(text=u'\u265D')
    elif piece_type=='C':
        Board_dict[(i, j)].configure(text=u'\u265E')
    elif piece_type=='R':
        Board_dict[(i, j)].configure(text=u'\u265A')
    elif piece_type=='D':
        Board_dict[(i, j)].configure(text=u'\u265B')

def show_chessboard():
    global root, Board_dict, fenetre
    root.withdraw()
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                Board_dict[(i,j)] = Button(cadre, bg='saddle brown', image=pixel, compound='center', font=my_font)
            else:
                Board_dict[(i,j)] = Button(cadre, bg='sandy brown', image=pixel, compound='center', font=my_font)
            if Chessboard[i][j]!=['','']:
                image_square_color(i, j)
            Board_dict[(i,j)].place(height=75, width=75, x=75*j, y=75*i)
            Board_dict[(i,j)].configure(command=lambda lin=i, col=j: Move(lin, col))
    fenetre.mainloop()

def All_fenetre_destroy():
    fenetre.destroy()
    root.destroy()

root=Tk()
fenetre=Toplevel()
pixel = PhotoImage(width=1, height=1)
cadre =  Frame(fenetre, width = 600, height = 750)
cadre.pack()
Indicate_turn=Button(cadre, text='White player turn', font=my_font_2)
Indicate_turn.place(x=150, y=600)
Escape=Button(cadre, text='Quit', command=All_fenetre_destroy, font=my_font_2)
Escape.place(x=200, y=650)
show_chessboard()

root.mainloop()











