WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTGRAY = (226,206,246)
GRAY = 	(175,80,229)
DARKGRAY = 	(91,6,114)
BLUE = (0, 0, 255)

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