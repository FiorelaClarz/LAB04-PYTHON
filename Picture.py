class Picture:
    def __init__(self, img):
        self.img = img

    def _invColor(self, char):
        inverse_colors = {
            ' ': '#',  # Ejemplo, se deben añadir todos los mapeos necesarios según el archivo colors.py
            '#': ' ',
            # Añadir otros colores y sus inversos
        }
        return inverse_colors.get(char, char)

    def verticalMirror(self):
        return Picture([line[::-1] for line in self.img])

    def horizontalMirror(self):
        return Picture(self.img[::-1])

    def negative(self):
        return Picture([''.join(self._invColor(char) for char in line) for line in self.img])

    def join(self, other):
        return Picture([self_line + other_line for self_line, other_line in zip(self.img, other.img)])

    def up(self, other):
        return Picture(other.img + self.img)

    def under(self, other):
        return Picture(self.img + other.img)

    def horizontalRepeat(self, n):
        return Picture([line * n for line in self.img])

    def verticalRepeat(self, n):
        return Picture(self.img * n)
