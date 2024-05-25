from interpreter import draw
from chessPictures import *

fila_1= (square.join(square.negative())).horizontalRepeat(4)
fila_2 = (square.negative().join(square)).horizontalRepeat(4)

resultado = fila_1
for i in range (3):
    if i%2==0 :
        resultado = resultado.under(fila_2)
    else :
        resultado = resultado.under(fila_1)
draw(resultado)

