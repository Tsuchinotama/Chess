from tkinter import *

nb_joueurs=0
trait='blanc'
couleur_joueur=' '
couleur_ordi=' '
dico_plat={}
case_dep=(-1,-1)
ma_police = "{courier new} 50"
ma_police2 = "{courier new} 25"

def N_lignes_vides(n):
    return [Ligne_vide_n(8) for i in range(n)]

def Ligne_vide_n(n):
    return [[' ',' '] for i in range(n)]

ligne_pieces=['T','C','F','D','R','F','C','T']

ligne_pieces_blanches=[[type,'blanc'] for type in ligne_pieces]

ligne_pieces_noires=[[type,'noir'] for type in ligne_pieces]

ligne_pions_blancs=[['P','blanc'] for i in range(8)]

ligne_pions_noirs=[['P','noir'] for i in range(8)]

Test_noir_ligne=Ligne_vide_n(8)
Test_blanc_ligne=Ligne_vide_n(8)

Test_noir_ligne[0]=['R', 'noir']
Test_noir_ligne[2]=['D', 'noir']
Test_blanc_ligne[3]=['P', 'blanc']
Test_blanc_ligne[7]=['R', 'blanc']

Test_echiquier_dep=[Test_noir_ligne, Test_blanc_ligne] + N_lignes_vides(6)
Test_echiquier_dep[6][3]=['P', 'noir']

echiquier_dep=[ligne_pieces_noires, ligne_pions_noirs] + N_lignes_vides(4) + [ligne_pions_blancs, ligne_pieces_blanches]

echiquier=echiquier_dep

def Eval(echiquier, ordi):
    score_ordi=0
    score_joueur=0
    for i in range(8):
        for j in range(8):
            case=echiquier[i][j]
            if case[1]==ordi:
                if case[0]=='P':
                    score_ordi=score_ordi+1
                elif case[0]=='T':
                    score_ordi=score_ordi+5
                elif case[0]=='F':
                    score_ordi=score_ordi+3
                elif case[0]=='C':
                    score_ordi=score_ordi+3
                elif case[0]=='D':
                    score_ordi=score_ordi+9
            else:
                if case[0]=='P':
                    score_joueur=score_joueur+1
                elif case[0]=='T':
                    score_joueur=score_joueur+5
                elif case[0]=='F':
                    score_joueur=score_joueur+3
                elif case[0]=='C':
                    score_joueur=score_joueur+3
                elif case[0]=='D':
                    score_joueur=score_joueur+9
    return score_ordi-score_joueur


# fonction renvoyant les mouvements possibles d'un pion suivant sa position de départ sans prendre en compte l'auto-mise en échec

def Mouvs_pieces(echiquier, pos_dep):
    lin=pos_dep[0]
    col=pos_dep[1]
    type_piece=echiquier[lin][col][0]
    if type_piece=='P':
        return Mouvs_pion(echiquier, pos_dep)
    elif type_piece=='T':
        return Mouvs_tour(echiquier, pos_dep)
    elif type_piece=='F':
        return Mouvs_fou(echiquier, pos_dep)
    elif type_piece=='C':
        return Mouvs_cavalier(echiquier, pos_dep)
    elif type_piece=='R':
        return Mouvs_roi(echiquier, pos_dep)
    elif type_piece=='D':
        return Mouvs_reine(echiquier, pos_dep)

def Mouvs_pion(echiquier, pos_dep):
    possible_moves=[]
    lin=pos_dep[0]
    col=pos_dep[1]
    if echiquier[lin][col][1]=='blanc':
        if lin>0:
            if echiquier[lin-1][col]==[' ',' ']:
                if lin==6 and echiquier[lin-2][col]==[' ',' ']:
                    possible_moves.append((lin-2,col))
                possible_moves.append((lin-1,col))
            if (col>0) and echiquier[lin-1][col-1][1]=='noir':
                    possible_moves.append((lin-1,col-1))
            if (col<7) and echiquier[lin-1][col+1][1]=='noir':
                    possible_moves.append((lin-1,col+1))
    else:
        if lin<7:
            if echiquier[lin+1][col]==[' ',' ']:
                if lin==1 and echiquier[lin+2][col]==[' ',' ']:
                    possible_moves.append((lin+2,col))
                possible_moves.append((lin+1,col))
            if (col>0) and echiquier[lin+1][col-1][1]=='blanc':
                possible_moves.append((lin+1,col+1))
            if (col<7) and echiquier[lin+1][col+1][1]=='blanc':
                possible_moves.append((lin+1,col+1))
    return possible_moves

def test_pion_promu(echiquier):
    case_promotion=(-1,-1)
    for i in [0,7]:
        for j in range(8):
            if echiquier[i][j][0]=='P':
                Promotion(i,j)

def Promotion(i, j):
    fenetre_promotion=Toplevel()
    Bouton_choix_tour=Button(fenetre_promotion, text='Tour', command=lambda promu='T', lin=i, col=j : Change_pion(lin, col, promu))
    Bouton_choix_fou=Button(fenetre_promotion, text='Fou', command=lambda promu='F', lin=i, col=j : Change_pion(lin, col, promu))
    Bouton_choix_cavalier=Button(fenetre_promotion, text='Cavalier', command=lambda promu='C', lin=i, col=j : Change_pion(lin, col, promu))
    Bouton_choix_reine=Button(fenetre_promotion, text='Reine', command=lambda promu='D', lin=i, col=j : Change_pion(lin, col, promu))
    Bouton_choix_tour.pack()
    Bouton_choix_fou.pack()
    Bouton_choix_cavalier.pack()
    Bouton_choix_reine.pack()


def Change_pion(lin, col, promu):
    if echiquier[lin][col][1]=='blanc':
        Change_pion_blanc(lin, col, promu)
        echiquier[lin][col][0]=promu
    else :
        Change_pion_noir(lin, col, promu)
        echiquier[lin][col][0]=promu

def Change_pion_blanc(i, j, promu):
    if promu=='T':
        dico_plat[(i, j)].configure(text=u'\u2656')
    elif promu=='F':
        dico_plat[(i, j)].configure(text=u'\u2657')
    elif promu=='C':
        dico_plat[(i, j)].configure(text=u'\u2658')
    elif promu=='D':
        dico_plat[(i, j)].configure(text=u'\u2655')


def Change_pion_noir(i, j, promu):
    if promu=='T':
        dico_plat[(i, j)].configure(text=u'\u265C')
    elif promu=='F':
        dico_plat[(i, j)].configure(text=u'\u265D')
    elif promu=='C':
        dico_plat[(i, j)].configure(text=u'\u265E')
    elif promu=='D':
        dico_plat[(i, j)].configure(text=u'\u265B')

# fonction renvoyant les mouvements possibles d'une tour suivant sa position de départ sans prendre en compte l'auto-mise en échec

def Mouvs_tour(echiquier, pos_dep):
    possible_moves=[]
    lin=pos_dep[0]
    col=pos_dep[1]
    lin_moins=lin
    while lin_moins>0 and echiquier[lin_moins-1][col][1]==' ':
        possible_moves.append((lin_moins-1,col))
        lin_moins=lin_moins-1
    if lin_moins>0 and echiquier[lin_moins-1][col][1]!=echiquier[lin][col][1]:
        possible_moves.append((lin_moins-1,col))
    lin_plus=lin
    while lin_plus<7 and echiquier[lin_plus+1][col][1]==' ':
        possible_moves.append((lin_plus+1,col))
        lin_plus=lin_plus+1
    if lin_plus>0 and echiquier[lin_plus-1][col][1]!=echiquier[lin][col][1]:
        possible_moves.append((lin_plus-1,col))
    col_moins=col
    while col_moins>0 and echiquier[lin][col_moins-1][1]==' ':
        possible_moves.append((lin,col_moins-1))
        col_moins=col_moins-1
    if col_moins>0 and echiquier[lin][col_moins-1][1]!=echiquier[lin][col][1]:
        possible_moves.append((lin,col_moins-1))
    col_plus=col
    while col_plus<7 and echiquier[lin][col_plus+1][1]==' ':
        possible_moves.append((lin,col_plus+1))
        col_plus=col_plus+1
    if col_plus<7 and echiquier[lin][col_plus+1][1]!=echiquier[lin][col][1]:
        possible_moves.append((lin,col_plus+1))
    return possible_moves

# fonction renvoyant les mouvements possibles d'un fou suivant sa position de départ sans prendre en compte l'auto-mise en échec

def Mouvs_fou(echiquier, pos_dep):
    possible_moves=[]
    lin=pos_dep[0]
    col=pos_dep[1]
    lin_NW=lin
    col_NW=col
    while lin_NW>0 and col_NW>0 and echiquier[lin_NW-1][col_NW-1][1]==' ':
        possible_moves.append((lin_NW-1,col_NW-1))
        lin_NW=lin_NW-1
        col_NW=col_NW-1
    if lin_NW>0 and col_NW>0 and echiquier[lin_NW-1][col_NW-1][1]!=echiquier[lin][col][1]:
        possible_moves.append((lin_NW-1,col_NW-1))
    lin_NE=lin
    col_NE=col
    while lin_NE>0 and col_NE<7 and echiquier[lin_NE-1][col_NE+1][1]==' ':
        possible_moves.append((lin_NE-1,col_NE+1))
        lin_NE=lin_NE-1
        col_NE=col_NE+1
    if lin_NE>0 and col_NE<7 and echiquier[lin_NE-1][col_NE+1][1]!=echiquier[lin][col][1]:
        possible_moves.append((lin_NE-1,col_NE+1))
    lin_SE=lin
    col_SE=col
    while lin_SE<7 and col_SE<7 and echiquier[lin_SE+1][col_SE+1][1]==' ':
        possible_moves.append((lin_SE+1,col_SE+1))
        lin_SE=lin_SE+1
        col_SE=col_SE+1
    if lin_SE<7 and col_SE<7 and echiquier[lin_SE+1][col_SE+1][1]!=echiquier[lin][col][1]:
        possible_moves.append((lin_SE+1,col_SE+1))
    lin_SW=lin
    col_SW=col
    while lin_SW<7 and col_SW>0 and echiquier[lin_SW+1][col_SW-1][1]==' ':
        possible_moves.append((lin_SW+1,col_SW-1))
        lin_SW=lin_SW+1
        col_SW=col_SW-1
    if lin_SW<7 and col_SW>0 and echiquier[lin_SW+1][col_SW-1][1]!=echiquier[lin][col][1]:
        possible_moves.append((lin_SW+1,col_SW-1))
    return possible_moves

# fonction renvoyant les mouvements possibles d'une dame suivant sa position de départ sans prendre en compte l'auto-mise en échec

def Mouvs_reine(echiquier, pos_dep):
    Mouvs_dame=Mouvs_fou(echiquier, pos_dep)
    Mouvs_dame.extend(pos for pos in Mouvs_tour(echiquier, pos_dep) if pos not in Mouvs_dame)
    return Mouvs_fou(echiquier, pos_dep) + Mouvs_tour(echiquier, pos_dep)

# fonction renvoyant les mouvements possibles d'un cavalier suivant sa position de départ sans prendre en compte l'auto-mise en échec

Deplacements_cavalier=[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

def Mouvs_cavalier(echiquier, pos_dep):
    possible_moves=[]
    lin=pos_dep[0]
    col=pos_dep[1]
    for mov in Deplacements_cavalier:
        if lin+mov[0]>-1 and lin+mov[0]<8 and col+mov[1]>-1 and col+mov[1]<8 and echiquier[lin+mov[0]][col+mov[1]][1]!=echiquier[lin][col][1]:
            possible_moves.append((lin+mov[0],col+mov[1]))
    return possible_moves

# fonction renvoyant les mouvements possibles d'un roi suivant sa position de départ

Deplacements_roi=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def Mouvs_roi(echiquier, pos_dep):
    possible_moves=[]
    lin=pos_dep[0]
    col=pos_dep[1]
    for mov in Deplacements_roi:
        arr_lin=lin+mov[0]
        arr_col=col+mov[1]
        if arr_lin<8 and arr_lin>-1 and arr_col<8 and arr_col>-1 and echiquier[arr_lin][arr_col][1]!=echiquier[lin][col][1]:
            possible_moves.append((arr_lin,arr_col))
    return possible_moves

# fonction renvoyant si le joueurs avec le trait s'est mis en auto-échec en 1er argument, s'il a mis le 2ème joueur en échec au roi en 3ème argument

def echec(echiquier, tour):
    auto_echec=False
    VS_echec=False
    for i in range(8):
        for j in range(8):
            test_case=echiquier[i][j]
            if not test_case[0]==' ':
                if test_case[0]=='T':
                    for arr_pos in Mouvs_tour(echiquier, (i,j)):
                        arr_case=echiquier[arr_pos[0]][arr_pos[1]]
                        if arr_case[0]=='R' and arr_case[1]!=test_case[1]:
                            if arr_case[1]==trait:
                                auto_echec=True
                            else:
                                VS_echec=True
                elif test_case[0]=='C':
                    for arr_pos in Mouvs_cavalier(echiquier, (i,j)):
                        arr_case=echiquier[arr_pos[0]][arr_pos[1]]
                        if arr_case[0]=='R' and arr_case[1]!=test_case[1]:
                            if arr_case[1]==trait:
                                auto_echec=True
                            else:
                                VS_echec=True
                elif test_case[0]=='F':
                    for arr_pos in Mouvs_fou(echiquier, (i,j)):
                        arr_case=echiquier[arr_pos[0]][arr_pos[1]]
                        if arr_case[0]=='R' and arr_case[1]!=test_case[1]:
                            if arr_case[1]==trait:
                                auto_echec=True
                            else:
                                VS_echec=True
                elif test_case[0]=='D':
                    for arr_pos in Mouvs_reine(echiquier, (i,j)):
                        arr_case=echiquier[arr_pos[0]][arr_pos[1]]
                        if arr_case[0]=='R' and arr_case[1]!=test_case[1]:
                            if arr_case[1]==trait:
                                auto_echec=True
                            else:
                                VS_echec=True
                elif test_case[0]=='P':
                    if test_case[1]=='blanc':
                        if i>0 and j>0 and echiquier[i-1][j-1][0]=='R' and echiquier[i-1][j-1][1]!=test_case[1]:
                            if test_case[1]!=trait:
                                auto_echec=True
                            else:
                                VS_echec=True
                        elif i>0 and j<7 and echiquier[i-1][j+1][0]=='R' and echiquier[i-1][j+1][1]!=test_case[1]:
                            if test_case[1]!=trait:
                                auto_echec=True
                            else:
                                VS_echec=True
                    else:
                        if i<7 and j>0 and echiquier[i+1][j-1][0]=='R' and echiquier[i+1][j-1][1]!=test_case[1]:
                            if test_case[1]!=trait:
                                auto_echec=True
                            else:
                                VS_echec=True
                        elif i<7 and j<7 and echiquier[i+1][j+1][0]=='R' and echiquier[i+1][j+1][1]!=test_case[1]:
                            if test_case[1]!=trait:
                                auto_echec=True
                            else:
                                VS_echec=True

    return (auto_echec, VS_echec)

# fonction renvoyant si le joueur qui a joué (qui a le trait) a mis l'adversaire mat (ne se lance qu'après avoir vérifié qu'on a un échec au roi simple)

def echec_et_mat(echiquier, trait):
    mat=True
    if trait=='blanc':
        trait='noir'
        for k in range(8):
            for l in range(8):
                test_case_mat=echiquier[k][l]
                if test_case_mat[1]==trait:
                    for mouvs in Mouvs_pieces(echiquier, (k,l)):
                        arr_case_test_mat=echiquier[mouvs[0]][mouvs[1]]
                        echiquier[mouvs[0]][mouvs[1]]=test_case_mat
                        echiquier[k][l]=[' ',' ']
                        if not echec(echiquier, trait)[0]:
                            mat=False
                            echiquier[k][l]=echiquier[mouvs[0]][mouvs[1]]
                            echiquier[mouvs[0]][mouvs[1]]=arr_case_test_mat
                            break
                        echiquier[k][l]=echiquier[mouvs[0]][mouvs[1]]
                        echiquier[mouvs[0]][mouvs[1]]=arr_case_test_mat
                    else:
                        continue
                    break
            else:
                continue
            break
    else:
        tour='blanc'
        for k in range(8):
            for l in range(8):
                test_case_mat=echiquier[k][l]
                if test_case_mat[1]==tour:
                    for mouvs in Mouvs_pieces(echiquier, (k,l)):
                        arr_case_test_mat=echiquier[mouvs[0]][mouvs[1]]
                        echiquier[mouvs[0]][mouvs[1]]=test_case_mat
                        echiquier[k][l]=[' ',' ']
                        if not echec(echiquier, tour)[0]:
                            mat=False
                            echiquier[k][l]=echiquier[mouvs[0]][mouvs[1]]
                            echiquier[mouvs[0]][mouvs[1]]=arr_case_test_mat
                            break
                        echiquier[k][l]=echiquier[mouvs[0]][mouvs[1]]
                        echiquier[mouvs[0]][mouvs[1]]=arr_case_test_mat
                    else:
                        continue
                    break
            else:
                continue
            break
    return mat

def Mouvement(nb_joueurs, pos):
    if nb_joueurs==1:
        Mouv_1_joueur(pos)
    else:
        Mouv_2_joueur(pos[0], pos[1])

def Mouv_1_joueur(pos):
    global case_dep, couleur_joueur, couleur_ordi
    lin=pos[0]
    col=pos[1]
    # if couleur_ordi=='blanc':
    #     couleur_joueur='noir'
    # else:
    #     couleur_joueur='blanc'
    if case_dep[0]<0:
        if echiquier[lin][col][1]==couleur_joueur:
            case_dep=(lin,col)
    elif (lin,col) in Mouvs_pieces(echiquier, case_dep):
        casearrprov=echiquier[lin][col]
        casedepprov=echiquier[case_dep[0]][case_dep[1]]
        echiquier[lin][col]=echiquier[case_dep[0]][case_dep[1]]
        echiquier[case_dep[0]][case_dep[1]]=[' ',' ']
        if echec(echiquier, couleur_joueur)[0]:
            echiquier[lin][col]=casearrprov
            echiquier[case_dep[0]][case_dep[1]]=casedepprov
            case_dep=(-1,-1)
        else:
            image_case_couleur(lin, col)
            dico_plat[(case_dep[0],case_dep[1])].configure(text=' ')
            case_dep=(-1,-1)
            if echec(echiquier, couleur_joueur)[1]:
                if echec_et_mat(echiquier, trait):
                    print('Le joueur a gagne')
                    root.destroy()
            (x_dep, y_dep, x_arr, y_arr)=Mouvement_ordi(echiquier)
            dico_plat[(x_dep,y_dep)].configure(text=' ')
            image_case_couleur(x_arr, y_arr)
    else:
        case_dep=(-1,-1)

def Mouv_2_joueur(lin, col):
    global case_dep, trait, fenetre
    if case_dep[0]<0:
        if echiquier[lin][col][1]==trait:
            case_dep=(lin,col)
    elif (lin,col) in Mouvs_pieces(echiquier, case_dep):
        casearrprov=echiquier[lin][col]
        casedepprov=echiquier[case_dep[0]][case_dep[1]]
        echiquier[lin][col]=echiquier[case_dep[0]][case_dep[1]]
        echiquier[case_dep[0]][case_dep[1]]=[' ',' ']
        if echec(echiquier, trait)[0]:
            echiquier[lin][col]=casearrprov
            echiquier[case_dep[0]][case_dep[1]]=casedepprov
            case_dep=(-1,-1)
        else:
            # if (test_pion_promu[0]):
            #     promotion_pion(test_pion_promu[1])
            image_case_couleur(lin, col)
            dico_plat[(case_dep[0],case_dep[1])].configure(text=' ')
            case_dep=(-1,-1)
            if echec(echiquier, trait)[1]:
                if echec_et_mat(echiquier, trait):
                    print('Le joueur %s a gagne' % trait)
                    Escape.configure(text='Le joueur %s a gagne. Quitter' % trait)
            test_pion_promu(echiquier)
            if trait=='blanc':
                trait='noir'
            else:
                trait='blanc'
    else:
        case_dep=(-1,-1)

def Mouvement_ordi(echiquier):
    Meilleur_score=-50
    echiquier_test=echiquier
    (x_ordi_dep_best, y_ordi_dep_best)=(-1, -1)
    (x_ordi_arr_best, y_ordi_arr_best)=(-1, -1)
    for i in range(8):
        for j in range(8):
            if echiquier_test[i][j][1]==couleur_ordi:
                case_dep_ordi=echiquier_test[i][j]
                for (lin, col) in Mouvs_pieces(echiquier_test, (i, j)):
                    case_arr_ordi=echiquier_test[lin][col]
                    echiquier_test[lin][col]=case_dep_ordi
                    echiquier_test[i][j]=[' ',' ']
                    if not echec(echiquier_test, couleur_ordi)[0]:
                        if echec_et_mat(echiquier_test, couleur_ordi):
                            print("Le ordi a gagne")
                            Espace.configure(text="Le ordi a gagne. Quitter ")
                            break
                        else:
                            for k in range(8):
                                for l in range(8):
                                    if echiquier_test[k][l][1]==couleur_joueur:
                                        case_dep_joueur=echiquier_test[k][l]
                                        for (linj, colj) in Mouvs_pieces(echiquier_test, (k, l)):
                                            Score=-40
                                            case_arr_joueur=echiquier_test[linj][colj]
                                            echiquier_test[linj][colj]=case_dep_joueur
                                            echiquier_test[k][l]=[' ',' ']
                                            if not echec(echiquier_test, couleur_joueur)[0]:
                                                Score=Eval(echiquier_test, couleur_ordi)
                                            echiquier_test[linj][colj]=case_arr_joueur
                                            echiquier_test[k][l]=case_dep_joueur
                                            if Score>Meilleur_score:
                                                Meilleur_score=Score
                                                (x_ordi_dep_best, y_ordi_dep_best)=(i, j)
                                                (x_ordi_arr_best, y_ordi_arr_best)=(lin, col)
                    echiquier_test[i][j]=case_dep_ordi
                    echiquier_test[lin][col]=case_arr_joueur
    echiquier[x_ordi_arr_best][y_ordi_arr_best]=echiquier[x_ordi_dep_best][y_ordi_dep_best]
    echiquier[x_ordi_dep_best][y_ordi_dep_best]=[' ', ' ']
    image_case_couleur(x_ordi_arr_best, y_ordi_arr_best)

    return(x_ordi_dep_best, y_ordi_dep_best, x_ordi_arr_best, y_ordi_arr_best)

def image_case_couleur(i, j):
    couleur_piece=echiquier[i][j][1]
    if couleur_piece=='blanc':
        image_case_blanche(i, j)
    else:
        image_case_noire(i, j)

def image_case_blanche(i, j):
    type_piece=echiquier[i][j][0]
    if type_piece=='P':
        dico_plat[(i, j)].configure(text=u'\u2659')
    elif type_piece=='T':
        dico_plat[(i, j)].configure(text=u'\u2656')
    elif type_piece=='F':
        dico_plat[(i, j)].configure(text=u'\u2657')
    elif type_piece=='C':
        dico_plat[(i, j)].configure(text=u'\u2658')
    elif type_piece=='R':
        dico_plat[(i, j)].configure(text=u'\u2654')
    elif type_piece=='D':
        dico_plat[(i, j)].configure(text=u'\u2655')

def image_case_noire(i, j):
    type_piece=echiquier[i][j][0]
    if type_piece=='P':
        dico_plat[(i, j)].configure(text=u'\u265F')
    elif type_piece=='T':
        dico_plat[(i, j)].configure(text=u'\u265C')
    elif type_piece=='F':
        dico_plat[(i, j)].configure(text=u'\u265D')
    elif type_piece=='C':
        dico_plat[(i, j)].configure(text=u'\u265E')
    elif type_piece=='R':
        dico_plat[(i, j)].configure(text=u'\u265A')
    elif type_piece=='D':
        dico_plat[(i, j)].configure(text=u'\u265B')

def affiche_echiquier_depart(nb_joueurs):
    # global root, dico_plat, fenetre
    global couleur_ordi, couleur_joueur
    root.withdraw()
    fenetre_choix.withdraw()
    fenetre.deiconify()
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                dico_plat[(i,j)] = Button(cadre, bg='saddle brown', image=pixel, compound='center', font=ma_police)
            else:
                dico_plat[(i,j)] = Button(cadre, bg='sandy brown', image=pixel, compound='center', font=ma_police)
            if echiquier[i][j]!=['','']:
                image_case_couleur(i, j)
            dico_plat[(i,j)].place(height=75, width=75, x=75*j, y=75*i)
            dico_plat[(i,j)].configure(command=lambda lin=i, col=j: Mouvement(nb_joueurs, (lin, col)))
    fenetre.mainloop()

def Fenetre_choix_couleur(nb_joueurs):
    fenetre_choix.deiconify()
    msg_choix_couleur=Label(fenetre_choix, text='Choix de la couleur du joueur')
    msg_choix_couleur.config(font=ma_police2)
    Bouton_choix_blanc=Button(fenetre_choix, font=ma_police2)
    Bouton_choix_noir=Button(fenetre_choix, font=ma_police2)
    Bouton_choix_blanc.configure(text='blanc', command=lambda n=nb_joueurs : Set_joueur_blanc(nb_joueurs))
    Bouton_choix_noir.configure(text='noir', command=lambda n=nb_joueurs : Set_joueur_noir(nb_joueurs))
    msg_choix_couleur.pack()
    Bouton_choix_blanc.pack()
    Bouton_choix_noir.pack()

def Set_1_joueurs():
    nb_joueurs=1
    Fenetre_choix_couleur(nb_joueurs)

def Set_2_joueurs():
    nb_joueurs=2
    affiche_echiquier_depart(nb_joueurs)

def Set_joueur_blanc(nb_joueurs):
    global couleur_joueur, couleur_ordi
    couleur_joueur='blanc'
    couleur_ordi='noir'
    affiche_echiquier_depart(nb_joueurs)

def Set_joueur_noir(nb_joueurs):
    global couleur_joueur, couleur_ordi
    couleur_joueur='noir'
    couleur_ordi='blanc'
    affiche_echiquier_depart(nb_joueurs)

def All_fenetre_destroy():
    fenetre.destroy()
    root.destroy()

root=Tk()
Bouton_choix_1=Button(root, text='1 joueurs', command=Set_1_joueurs, font=ma_police2)
Bouton_choix_2=Button(root, text='2 joueurs', command=Set_2_joueurs, font=ma_police2)
Bouton_choix_1.pack()
Bouton_choix_2.pack()
fenetre = Toplevel()
fenetre_choix=Toplevel()
pixel = PhotoImage(width=1, height=1)
cadre =  Frame(fenetre, width = 600, height = 700)
cadre.pack()
Escape=Button(cadre, text='Quitter', command=All_fenetre_destroy, font=ma_police2)
Escape.place(x=200, y=600)
fenetre.withdraw()
fenetre_choix.withdraw()

root.mainloop()











