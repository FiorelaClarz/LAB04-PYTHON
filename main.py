from Picture import Picture
from pieces import rock, knight, bishop, queen, king, square
from interpreter import draw

# Crear objetos Picture
rock_pic = Picture(rock)
knight_pic = Picture(knight)
bishop_pic = Picture(bishop)
queen_pic = Picture(queen)
king_pic = Picture(king)
square_pic = Picture(square)

# Probar métodos
print("Vertical Mirror:")
draw(rock_pic.verticalMirror())

print("\nHorizontal Mirror:")
draw(knight_pic.horizontalMirror())

print("\nNegative:")
draw(rock_pic.negative())

print("\nJoin:")
draw(rock_pic.join(knight_pic))

print("\nUp:")
draw(knight_pic.up(rock_pic))

print("\nUnder:")
draw(rock_pic.under(knight_pic))

print("\nHorizontal Repeat:")
draw(rock_pic.horizontalRepeat(3))

print("\nVertical Repeat:")
draw(rock_pic.verticalRepeat(2))
