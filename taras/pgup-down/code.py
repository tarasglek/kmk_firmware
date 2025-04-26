# https://circuitpython.org/board/waveshare_esp32_s3_zero/
print("Starting")
from kmk.hid import HIDModes
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.tapdance import TapDance
from kmk.scanners import DiodeOrientation


# Pin is now deinitialized after exiting the 'with' block

keyboard = KMKKeyboard()

# --- Modules ---
tapdance = TapDance()
keyboard.modules.append(tapdance)

# Row pin IO12
keyboard.row_pins = (board.IO12,)
# Column pins IO8, IO9, IO10, IO11
keyboard.col_pins = (board.IO8, board.IO9, board.IO10, board.IO11)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define Tap Dance key: Tap for Alt+Left (Back), Hold for Ctrl+W (Close)
BACK_OR_CLOSE = KC.TD(KC.LALT(KC.LEFT), KC.LCTL(KC.W))

keyboard.keymap = [
    # Reordered to match physical wiring: IO8=2, IO9=1, IO10=4, IO11=3
    [KC.SPACE, KC.PGDN, KC.PGUP, BACK_OR_CLOSE] # IO11 -> TapDance Key
]

if __name__ == '__main__':
    keyboard.go()
#    keyboard.go(hid_type=HIDModes.BLE, secondary_hid_type=HIDModes.USB, ble_name='1234Keyboard')

