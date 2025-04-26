print("Starting")

import board

print(dir(board))

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Row pin IO12
keyboard.row_pins = (board.GP12,)
# Column pins IO8, IO9, IO10, IO11
keyboard.col_pins = (board.GP8, board.GP9, board.GP10, board.GP11)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4] # Keys for row 0, columns 0-3
]

if __name__ == '__main__':
    keyboard.go()
