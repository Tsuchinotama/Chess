from tkinter import *

nbr_players=0
turn='white'
human_player_color=' '
computer_color=' '
dict_chessboard={}
dep_square=(-1,-1)
my_font = "{courier new} 50"
my_font2 = "{courier new} 25"

def N_empty_lines(n):
    return [Empty_line_of_n(8) for i in range(n)]

def Empty_line_of_n(n):
    return [[' ',' '] for i in range(n)]

pieces_line=['T','C','F','D','R','F','C','T']

line_white_pieces=[[type,'white'] for type in pieces_line]

line_black_pieces=[[type,'black'] for type in pieces_line]

line_white_pawns=[['P','white'] for i in range(8)]

line_black_pawns=[['P','black'] for i in range(8)]

Test_black_line=Empty_line_of_n(8)
Test_white_ligne=Empty_line_of_n(8)

Test_black_line[0]=['R', 'black']
Test_black_line[2]=['D', 'black']
Test_white_ligne[3]=['P', 'white']
Test_white_ligne[7]=['R', 'white']

Test_dep_cheesboard=[Test_black_line, Test_white_ligne] + N_empty_lines(6)
Test_dep_cheesboard[6][3]=['P', 'black']

dep_chessboard=[line_black_pieces, line_black_pawns] + N_empty_lines(4) + [line_white_pawns, line_white_pieces]

chessboard=dep_chessboard

def Eval(chessboard, computer):
    score_computer=0
    score_player=0
    for i in range(8):
        for j in range(8):
            square=chessboard[i][j]
            if square[1]==computer:
                if square[0]=='P':
                    score_computer=score_computer+1
                elif square[0]=='T':
                    score_computer=score_computer+5
                elif square[0]=='F':
                    score_computer=score_computer+3
                elif square[0]=='C':
                    score_computer=score_computer+3
                elif square[0]=='D':
                    score_computer=score_computer+9
            else:
                if square[0]=='P':
                    score_player=score_player+1
                elif square[0]=='T':
                    score_player=score_player+5
                elif square[0]=='F':
                    score_player=score_player+3
                elif square[0]=='C':
                    score_player=score_player+3
                elif square[0]=='D':
                    score_player=score_player+9
    return score_computer-score_player


# fonction renvoyant les Moves possibles d'un pawn suivant sa position de départ sans prendre en compte l'auto-mise en échec

def Pieces_moves(chessboard, dep_pos):
    lin=dep_pos[0]
    col=dep_pos[1]
    type_piece=chessboard[lin][col][0]
    if type_piece=='P':
        return Pawn_moves(chessboard, dep_pos)
    elif type_piece=='T':
        return Rook_moves(chessboard, dep_pos)
    elif type_piece=='F':
        return Bishop_moves(chessboard, dep_pos)
    elif type_piece=='C':
        return Knight_moves(chessboard, dep_pos)
    elif type_piece=='R':
        return King_moves(chessboard, dep_pos)
    elif type_piece=='D':
        return Queen_moves(chessboard, dep_pos)

def Pawn_moves(chessboard, dep_pos):
    possible_moves=[]
    lin=dep_pos[0]
    col=dep_pos[1]
    if chessboard[lin][col][1]=='white':
        if lin>0:
            if chessboard[lin-1][col]==[' ',' ']:
                if lin==6 and chessboard[lin-2][col]==[' ',' ']:
                    possible_moves.append((lin-2,col))
                possible_moves.append((lin-1,col))
            if (col>0) and chessboard[lin-1][col-1][1]=='black':
                    possible_moves.append((lin-1,col-1))
            if (col<7) and chessboard[lin-1][col+1][1]=='black':
                    possible_moves.append((lin-1,col+1))
    else:
        if lin<7:
            if chessboard[lin+1][col]==[' ',' ']:
                if lin==1 and chessboard[lin+2][col]==[' ',' ']:
                    possible_moves.append((lin+2,col))
                possible_moves.append((lin+1,col))
            if (col>0) and chessboard[lin+1][col-1][1]=='white':
                possible_moves.append((lin+1,col+1))
            if (col<7) and chessboard[lin+1][col+1][1]=='white':
                possible_moves.append((lin+1,col+1))
    return possible_moves

def Test_promote_pawn(chessboard):
    square_promotion=(-1,-1)
    for i in [0,7]:
        for j in range(8):
            if chessboard[i][j][0]=='P':
                Promotion(i,j)

def Promotion(i, j):
    promo_window=Toplevel()
    Rook_choice_button=Button(promo_window, text='Rook', command=lambda promoted='T', lin=i, col=j : Change_pawn(lin, col, promoted))
    Bishop_choice_button=Button(promo_window, text='Bishop', command=lambda promoted='F', lin=i, col=j : Change_pawn(lin, col, promoted))
    Knight_choice_button=Button(promo_window, text='Knight', command=lambda promoted='C', lin=i, col=j : Change_pawn(lin, col, promoted))
    Queen_choice_button=Button(promo_window, text='Queen', command=lambda promoted='D', lin=i, col=j : Change_pawn(lin, col, promoted))
    Rook_choice_button.pack()
    Bishop_choice_button.pack()
    Knight_choice_button.pack()
    Queen_choice_button.pack()


def Change_pawn(lin, col, promoted):
    if chessboard[lin][col][1]=='white':
        Change_pawn_white(lin, col, promoted)
        chessboard[lin][col][0]=promoted
    else :
        Change_pawn_black(lin, col, promoted)
        chessboard[lin][col][0]=promoted

def Change_pawn_white(i, j, promoted):
    if promoted=='T':
        dict_chessboard[(i, j)].configure(text=u'\u2656')
    elif promoted=='F':
        dict_chessboard[(i, j)].configure(text=u'\u2657')
    elif promoted=='C':
        dict_chessboard[(i, j)].configure(text=u'\u2658')
    elif promoted=='D':
        dict_chessboard[(i, j)].configure(text=u'\u2655')


def Change_pawn_black(i, j, promoted):
    if promoted=='T':
        dict_chessboard[(i, j)].configure(text=u'\u265C')
    elif promoted=='F':
        dict_chessboard[(i, j)].configure(text=u'\u265D')
    elif promoted=='C':
        dict_chessboard[(i, j)].configure(text=u'\u265E')
    elif promoted=='D':
        dict_chessboard[(i, j)].configure(text=u'\u265B')

# fonction renvoyant les Moves possibles d'une Rook suivant sa position de départ sans prendre en compte l'auto-mise en échec

def Rook_moves(chessboard, dep_pos):
    possible_moves=[]
    lin=dep_pos[0]
    col=dep_pos[1]
    lin_moins=lin
    while lin_moins>0 and chessboard[lin_moins-1][col][1]==' ':
        possible_moves.append((lin_moins-1,col))
        lin_moins=lin_moins-1
    if lin_moins>0 and chessboard[lin_moins-1][col][1]!=chessboard[lin][col][1]:
        possible_moves.append((lin_moins-1,col))
    lin_plus=lin
    while lin_plus<7 and chessboard[lin_plus+1][col][1]==' ':
        possible_moves.append((lin_plus+1,col))
        lin_plus=lin_plus+1
    if lin_plus>0 and chessboard[lin_plus-1][col][1]!=chessboard[lin][col][1]:
        possible_moves.append((lin_plus-1,col))
    col_moins=col
    while col_moins>0 and chessboard[lin][col_moins-1][1]==' ':
        possible_moves.append((lin,col_moins-1))
        col_moins=col_moins-1
    if col_moins>0 and chessboard[lin][col_moins-1][1]!=chessboard[lin][col][1]:
        possible_moves.append((lin,col_moins-1))
    col_plus=col
    while col_plus<7 and chessboard[lin][col_plus+1][1]==' ':
        possible_moves.append((lin,col_plus+1))
        col_plus=col_plus+1
    if col_plus<7 and chessboard[lin][col_plus+1][1]!=chessboard[lin][col][1]:
        possible_moves.append((lin,col_plus+1))
    return possible_moves

# fonction renvoyant les Moves possibles d'un Bishop suivant sa position de départ sans prendre en compte l'auto-mise en échec

def Bishop_moves(chessboard, dep_pos):
    possible_moves=[]
    lin=dep_pos[0]
    col=dep_pos[1]
    lin_NW=lin
    col_NW=col
    while lin_NW>0 and col_NW>0 and chessboard[lin_NW-1][col_NW-1][1]==' ':
        possible_moves.append((lin_NW-1,col_NW-1))
        lin_NW=lin_NW-1
        col_NW=col_NW-1
    if lin_NW>0 and col_NW>0 and chessboard[lin_NW-1][col_NW-1][1]!=chessboard[lin][col][1]:
        possible_moves.append((lin_NW-1,col_NW-1))
    lin_NE=lin
    col_NE=col
    while lin_NE>0 and col_NE<7 and chessboard[lin_NE-1][col_NE+1][1]==' ':
        possible_moves.append((lin_NE-1,col_NE+1))
        lin_NE=lin_NE-1
        col_NE=col_NE+1
    if lin_NE>0 and col_NE<7 and chessboard[lin_NE-1][col_NE+1][1]!=chessboard[lin][col][1]:
        possible_moves.append((lin_NE-1,col_NE+1))
    lin_SE=lin
    col_SE=col
    while lin_SE<7 and col_SE<7 and chessboard[lin_SE+1][col_SE+1][1]==' ':
        possible_moves.append((lin_SE+1,col_SE+1))
        lin_SE=lin_SE+1
        col_SE=col_SE+1
    if lin_SE<7 and col_SE<7 and chessboard[lin_SE+1][col_SE+1][1]!=chessboard[lin][col][1]:
        possible_moves.append((lin_SE+1,col_SE+1))
    lin_SW=lin
    col_SW=col
    while lin_SW<7 and col_SW>0 and chessboard[lin_SW+1][col_SW-1][1]==' ':
        possible_moves.append((lin_SW+1,col_SW-1))
        lin_SW=lin_SW+1
        col_SW=col_SW-1
    if lin_SW<7 and col_SW>0 and chessboard[lin_SW+1][col_SW-1][1]!=chessboard[lin][col][1]:
        possible_moves.append((lin_SW+1,col_SW-1))
    return possible_moves

# fonction renvoyant les Moves possibles d'une dame suivant sa position de départ sans prendre en compte l'auto-mise en échec

def Queen_moves(chessboard, dep_pos):
    Queen_moves=Bishop_moves(chessboard, dep_pos)
    Queen_moves.extend(pos for pos in Rook_moves(chessboard, dep_pos) if pos not in Queen_moves)
    return Bishop_moves(chessboard, dep_pos) + Rook_moves(chessboard, dep_pos)

# fonction renvoyant les Moves possibles d'un Knight suivant sa position de départ sans prendre en compte l'auto-mise en échec

Knight_possible_moves=[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

def Knight_moves(chessboard, dep_pos):
    possible_moves=[]
    lin=dep_pos[0]
    col=dep_pos[1]
    for mov in Knight_possible_moves:
        if lin+mov[0]>-1 and lin+mov[0]<8 and col+mov[1]>-1 and col+mov[1]<8 and chessboard[lin+mov[0]][col+mov[1]][1]!=chessboard[lin][col][1]:
            possible_moves.append((lin+mov[0],col+mov[1]))
    return possible_moves

# fonction renvoyant les Moves possibles d'un roi suivant sa position de départ

King_possible_moves=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def King_moves(chessboard, dep_pos):
    possible_moves=[]
    lin=dep_pos[0]
    col=dep_pos[1]
    for mov in King_possible_moves:
        arr_lin=lin+mov[0]
        arr_col=col+mov[1]
        if arr_lin<8 and arr_lin>-1 and arr_col<8 and arr_col>-1 and chessboard[arr_lin][arr_col][1]!=chessboard[lin][col][1]:
            possible_moves.append((arr_lin,arr_col))
    return possible_moves

# fonction renvoyant si le joueurs avec le turn s'est mis en auto-échec en 1er argument, s'il a mis le 2ème joueur en échec au roi en 3ème argument

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

# fonction renvoyant si le joueur qui a joué (qui a le turn) a mis l'adversaire mat (ne se lance qu'après avoir vérifié qu'on a un échec au roi simple)

def checkmate(chessboard, turn):
    mat=True
    if turn=='white':
        turn='black'
        for k in range(8):
            for l in range(8):
                test_square_mat=chessboard[k][l]
                if test_square_mat[1]==turn:
                    for mouvs in Pieces_moves(chessboard, (k,l)):
                        arr_square_test_mat=chessboard[mouvs[0]][mouvs[1]]
                        chessboard[mouvs[0]][mouvs[1]]=test_square_mat
                        chessboard[k][l]=[' ',' ']
                        if not check(chessboard, turn)[0]:
                            mat=False
                            chessboard[k][l]=chessboard[mouvs[0]][mouvs[1]]
                            chessboard[mouvs[0]][mouvs[1]]=arr_square_test_mat
                            break
                        chessboard[k][l]=chessboard[mouvs[0]][mouvs[1]]
                        chessboard[mouvs[0]][mouvs[1]]=arr_square_test_mat
                    else:
                        continue
                    break
            else:
                continue
            break
    else:
        Rook='white'
        for k in range(8):
            for l in range(8):
                test_square_mat=chessboard[k][l]
                if test_square_mat[1]==Rook:
                    for mouvs in Pieces_moves(chessboard, (k,l)):
                        arr_square_test_mat=chessboard[mouvs[0]][mouvs[1]]
                        chessboard[mouvs[0]][mouvs[1]]=test_square_mat
                        chessboard[k][l]=[' ',' ']
                        if not check(chessboard, Rook)[0]:
                            mat=False
                            chessboard[k][l]=chessboard[mouvs[0]][mouvs[1]]
                            chessboard[mouvs[0]][mouvs[1]]=arr_square_test_mat
                            break
                        chessboard[k][l]=chessboard[mouvs[0]][mouvs[1]]
                        chessboard[mouvs[0]][mouvs[1]]=arr_square_test_mat
                    else:
                        continue
                    break
            else:
                continue
            break
    return mat

def Move(nbr_players, pos):
    if nbr_players==1:
        Move_1_player(pos)
    else:
        Mouv_2_joueur(pos[0], pos[1])

def Move_1_player(pos):
    global dep_square, human_player_color, computer_color
    lin=pos[0]
    col=pos[1]
    # if computer_color=='white':
    #     human_player_color='black'
    # else:
    #     human_player_color='white'
    if dep_square[0]<0:
        if chessboard[lin][col][1]==human_player_color:
            dep_square=(lin,col)
    elif (lin,col) in Pieces_moves(chessboard, dep_square):
        squarearrtemp=chessboard[lin][col]
        squaredeptemp=chessboard[dep_square[0]][dep_square[1]]
        chessboard[lin][col]=chessboard[dep_square[0]][dep_square[1]]
        chessboard[dep_square[0]][dep_square[1]]=[' ',' ']
        if check(chessboard, human_player_color)[0]:
            chessboard[lin][col]=squarearrtemp
            chessboard[dep_square[0]][dep_square[1]]=squaredeptemp
            dep_square=(-1,-1)
        else:
            color_square_image(lin, col)
            dict_chessboard[(dep_square[0],dep_square[1])].configure(text=' ')
            dep_square=(-1,-1)
            if check(chessboard, human_player_color)[1]:
                if checkmate(chessboard, turn):
                    print('Le joueur a gagne')
                    root.destroy()
            (x_dep, y_dep, x_arr, y_arr)=Move_computer(chessboard)
            dict_chessboard[(x_dep,y_dep)].configure(text=' ')
            color_square_image(x_arr, y_arr)
    else:
        dep_square=(-1,-1)

def Mouv_2_joueur(lin, col):
    global dep_square, turn, window
    if dep_square[0]<0:
        if chessboard[lin][col][1]==turn:
            dep_square=(lin,col)
    elif (lin,col) in Pieces_moves(chessboard, dep_square):
        squarearrtemp=chessboard[lin][col]
        squaredeptemp=chessboard[dep_square[0]][dep_square[1]]
        chessboard[lin][col]=chessboard[dep_square[0]][dep_square[1]]
        chessboard[dep_square[0]][dep_square[1]]=[' ',' ']
        if check(chessboard, turn)[0]:
            chessboard[lin][col]=squarearrtemp
            chessboard[dep_square[0]][dep_square[1]]=squaredeptemp
            dep_square=(-1,-1)
        else:
            # if (Test_promote_pawn[0]):
            #     promotion_pawn(Test_promote_pawn[1])
            color_square_image(lin, col)
            dict_chessboard[(dep_square[0],dep_square[1])].configure(text=' ')
            dep_square=(-1,-1)
            if check(chessboard, turn)[1]:
                if checkmate(chessboard, turn):
                    print('Player %s won' % turn)
                    Escape.configure(text='Player %s won. Quit' % turn)
            Test_promote_pawn(chessboard)
            if turn=='white':
                turn='black'
            else:
                turn='white'
    else:
        dep_square=(-1,-1)

def Move_computer(chessboard):
    Best_score=-50
    chessboard_test=chessboard
    (x_computer_dep_best, y_computer_dep_best)=(-1, -1)
    (x_computer_arr_best, y_computer_arr_best)=(-1, -1)
    for i in range(8):
        for j in range(8):
            if chessboard_test[i][j][1]==computer_color:
                computer_depart_square=chessboard_test[i][j]
                for (lin, col) in Pieces_moves(chessboard_test, (i, j)):
                    square_arr_computer=chessboard_test[lin][col]
                    chessboard_test[lin][col]=computer_depart_square
                    chessboard_test[i][j]=[' ',' ']
                    if not check(chessboard_test, computer_color)[0]:
                        if checkmate(chessboard_test, computer_color):
                            print("Computer wins")
                            Espace.configure(text="Computer wins. Quit ")
                            break
                        else:
                            for k in range(8):
                                for l in range(8):
                                    if chessboard_test[k][l][1]==human_player_color:
                                        player_depart_square=chessboard_test[k][l]
                                        for (lin_player, col_player) in Pieces_moves(chessboard_test, (k, l)):
                                            Score=-40
                                            player_arrival_square=chessboard_test[lin_player][col_player]
                                            chessboard_test[lin_player][col_player]=player_depart_square
                                            chessboard_test[k][l]=[' ',' ']
                                            if not check(chessboard_test, human_player_color)[0]:
                                                Score=Eval(chessboard_test, computer_color)
                                            chessboard_test[lin_player][col_player]=player_arrival_square
                                            chessboard_test[k][l]=player_depart_square
                                            if Score>Best_score:
                                                Best_score=Score
                                                (x_computer_dep_best, y_computer_dep_best)=(i, j)
                                                (x_computer_arr_best, y_computer_arr_best)=(lin, col)
                    chessboard_test[i][j]=computer_depart_square
                    chessboard_test[lin][col]=player_arrival_square
    chessboard[x_computer_arr_best][y_computer_arr_best]=chessboard[x_computer_dep_best][y_computer_dep_best]
    chessboard[x_computer_dep_best][y_computer_dep_best]=[' ', ' ']
    color_square_image(x_computer_arr_best, y_computer_arr_best)

    return(x_computer_dep_best, y_computer_dep_best, x_computer_arr_best, y_computer_arr_best)

def color_square_image(i, j):
    piece_color=chessboard[i][j][1]
    if piece_color=='white':
        image_square_white(i, j)
    else:
        image_square_blacke(i, j)

def image_square_white(i, j):
    type_piece=chessboard[i][j][0]
    if type_piece=='P':
        dict_chessboard[(i, j)].configure(text=u'\u2659')
    elif type_piece=='T':
        dict_chessboard[(i, j)].configure(text=u'\u2656')
    elif type_piece=='F':
        dict_chessboard[(i, j)].configure(text=u'\u2657')
    elif type_piece=='C':
        dict_chessboard[(i, j)].configure(text=u'\u2658')
    elif type_piece=='R':
        dict_chessboard[(i, j)].configure(text=u'\u2654')
    elif type_piece=='D':
        dict_chessboard[(i, j)].configure(text=u'\u2655')

def image_square_blacke(i, j):
    type_piece=chessboard[i][j][0]
    if type_piece=='P':
        dict_chessboard[(i, j)].configure(text=u'\u265F')
    elif type_piece=='T':
        dict_chessboard[(i, j)].configure(text=u'\u265C')
    elif type_piece=='F':
        dict_chessboard[(i, j)].configure(text=u'\u265D')
    elif type_piece=='C':
        dict_chessboard[(i, j)].configure(text=u'\u265E')
    elif type_piece=='R':
        dict_chessboard[(i, j)].configure(text=u'\u265A')
    elif type_piece=='D':
        dict_chessboard[(i, j)].configure(text=u'\u265B')

def show_chessboard_dep(nbr_players):
    # global root, dict_chessboard, window
    global computer_color, human_player_color
    root.withdraw()
    choice_window.withdraw()
    window.deiconify()
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                dict_chessboard[(i,j)] = Button(cadre, bg='saddle brown', image=pixel, compound='center', font=my_font)
            else:
                dict_chessboard[(i,j)] = Button(cadre, bg='sandy brown', image=pixel, compound='center', font=my_font)
            if chessboard[i][j]!=['','']:
                color_square_image(i, j)
            dict_chessboard[(i,j)].place(height=75, width=75, x=75*j, y=75*i)
            dict_chessboard[(i,j)].configure(command=lambda lin=i, col=j: Move(nbr_players, (lin, col)))
    window.mainloop()

def color_choice_window(nbr_players):
    choice_window.deiconify()
    color_choice_msg=Label(choice_window, text='Choose the human player color')
    color_choice_msg.config(font=my_font2)
    choice_white_button=Button(choice_window, font=my_font2)
    choice_black_button=Button(choice_window, font=my_font2)
    choice_white_button.configure(text='white', command=lambda n=nbr_players : Set_human_player_white(nbr_players))
    choice_black_button.configure(text='black', command=lambda n=nbr_players : Set_human_player_black(nbr_players))
    color_choice_msg.pack()
    choice_white_button.pack()
    choice_black_button.pack()

def Set_1_player():
    nbr_players=1
    color_choice_window(nbr_players)

def Set_2_players():
    nbr_players=2
    show_chessboard_dep(nbr_players)

def Set_human_player_white(nbr_players):
    global human_player_color, computer_color
    human_player_color='white'
    computer_color='black'
    show_chessboard_dep(nbr_players)

def Set_human_player_black(nbr_players):
    global human_player_color, computer_color
    human_player_color='black'
    computer_color='white'
    show_chessboard_dep(nbr_players)

def All_window_destroy():
    window.destroy()
    root.destroy()

root=Tk()
button_choice_1_player=Button(root, text='1 player', command=Set_1_player, font=my_font2)
button_choice_2_players=Button(root, text='2 players', command=Set_2_players, font=my_font2)
button_choice_1_player.pack()
button_choice_2_players.pack()
window = Toplevel()
choice_window=Toplevel()
pixel = PhotoImage(width=1, height=1)
cadre =  Frame(window, width = 600, height = 700)
cadre.pack()
Escape=Button(cadre, text='Quit', command=All_window_destroy, font=my_font2)
Escape.place(x=200, y=600)
window.withdraw()
choice_window.withdraw()

root.mainloop()











