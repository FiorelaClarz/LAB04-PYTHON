from interpreter import draw
from chessPictures import *

def unir(piece,casilleroBlanco):
    new_img=[]
    casilleroBlanco_color=casilleroBlanco.img[0][0]
    for row in piece.img:
        new_row=row.replace(" ",casilleroBlanco_color)
        new_img.append(new_row)
    return Picture(new_img)

casilleroBlanco=square
casilleroNegro=square.negative()

# Crear piezas en celdas alternadas
rock_black = unir(rock, casilleroNegro)
knight_white = unir(knight, casilleroBlanco)
bishop_black = unir(bishop, casilleroNegro)
king_black = unir(king, casilleroNegro)
queen_white = unir(queen, casilleroBlanco)
bishop_white = unir(bishop, casilleroBlanco)
knight_black = unir(knight, casilleroNegro)
rock_white = unir(rock, casilleroBlanco)
pawn_white = unir(pawn, casilleroBlanco)
pawn_black = unir(pawn, casilleroNegro)

# Crear fila 1 (torres, caballos, alfiles, rey, reina)
fila_1 = rock_black.join(knight_white).join(bishop_black).join(queen_white).join(king_black).join(bishop_white).join(knight_black).join(rock_white)

# Crear fila 2 (peones)
fila_2 = pawn_white.join(pawn_black).horizontalRepeat(4)


# Crear filas vacías (alternando celdas)
fila_3 = casilleroBlanco.join(casilleroNegro).horizontalRepeat(4)
fila_4 = fila_3.negative()
fila_3_4 = fila_3.under(fila_4)


# Combinar filas para crear la mitad del tablero
mitad_tableroB=fila_1.up(fila_2).up(fila_3_4)
mitad_tableroN=fila_3_4.up(fila_2.negative()).up(fila_1.negative())
# draw(fila_3)

# Unir ambas mitades para crear el tablero completo
tablero=mitad_tableroB.up(mitad_tableroN)

# Dibujar el tablero
draw(tablero)