# https://circuitpython.org/board/waveshare_esp32_s3_zero/
print("Starting")
from kmk.hid import HIDModes
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.scanners import DiodeOrientation


# Pin is now deinitialized after exiting the 'with' block

keyboard = KMKKeyboard()

# --- Modules ---
# Use HoldTap for tap-vs-hold behavior
holdtap = HoldTap()
# Optional: Set hold time (milliseconds). Default is usually 300.
# holdtap.tap_time = 250
keyboard.modules.append(holdtap)

# Row pin IO12
keyboard.row_pins = (board.IO12,)
# Column pins IO8, IO9, IO10, IO11
keyboard.col_pins = (board.IO8, board.IO9, board.IO10, board.IO11)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Use KC.HT: Tap=Alt+Left, Hold=Ctrl+W. prefer_hold=False triggers hold if held past tap_time.
BACK_OR_CLOSE = KC.HT(KC.LALT(KC.LEFT), KC.LCTL(KC.W), prefer_hold=False)

keyboard.keymap = [
    # Reordered to match physical wiring: IO8=2, IO9=1, IO10=4, IO11=3
    [KC.SPACE, KC.PGDN, KC.PGUP, BACK_OR_CLOSE] # IO11 -> TapDance Key
]

if __name__ == '__main__':
    keyboard.go()
#    keyboard.go(hid_type=HIDModes.BLE, secondary_hid_type=HIDModes.USB, ble_name='1234Keyboard')

