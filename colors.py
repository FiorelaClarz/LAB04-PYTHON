WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTGRAY = (226,206,246)
GRAY = 	(175,80,229)
DARKGRAY = 	(91,6,114)
BLUE = 	(77,0,92)

color = {
  '_': LIGHTGRAY,
  '=': GRAY,
  '.': WHITE,
  '@': BLACK,
  '#': DARKGRAY,
  ' ': BLUE,
}
inverter = {
  '_': '=',
  '=': '_',
  '.': '@',
  '@': '.',
}