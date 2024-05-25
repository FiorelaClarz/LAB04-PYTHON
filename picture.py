from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    new_img=[]
    for row in self.img:
      new_img.append(row[::-1])
    return Picture(new_img)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    new_img=self.img[::-1]
    return Picture(new_img)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative_img=[]
    for row in self.img:
      negative_row=""
      for char in row:
        negative_char=self.invColor(char)
        negative_row+=negative_char
      negative_img.append(negative_row)
    return Picture(negative_img)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    new_img=[]
    numFilas=len(self.img)
    for i in range(numFilas):
      fila=self.img[i]+p.img[i]
      new_img.append(fila)
    return Picture(new_img)

  def up(self, p):
    new_img=[]
    for row in p.img:
      new_img.append(row)
    for row in self.img:
      new_img.append(row)
    return Picture(new_img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    new_img=[]
    for row in self.img:
      new_img.append(row)
    for row in p.img:
      new_img.append(row)
    return Picture(new_img)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    new_img=[]
    for row in self.img:
      new_img.append(row*n)
    return Picture(new_img)

  def verticalRepeat(self, n):
    return Picture(self.img*n)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)