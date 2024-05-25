from interpreter import draw
from chessPictures import *

fila_1 = knight.join(knight.negative())
fila_2 = fila_1.verticalMirror()
resultado = fila_1.under(fila_2)
draw(resultado)