print("Starting")

from time import sleep

from Firmware.kmk.modules import holdtap, layers
import board
import digitalio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers




keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, holdtap, encoder_handler]

keyboard.col_pins = (board.GP0, board.GP1, board.GP4)
keyboard.row_pins = (board.GP5, board.GP3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())

# Motor pins/setups thingy

Mot1a = digitalio.DigitalInOut(board.GP18)
Mot1b = digitalio.DigitalInOut(board.GP8)
Mot2a = digitalio.DigitalInOut(board.GP9)
Mot2b = digitalio.DigitalInOut(board.GP17)
Mot1a.direction = digitalio.Direction.OUTPUT
Mot1b.direction = digitalio.Direction.OUTPUT
Mot2a.direction = digitalio.Direction.OUTPUT
Mot2b.direction = digitalio.Direction.OUTPUT
Mot1a.value = False
Mot1b.value = False
Mot2a.value = False
Mot2b.value = False


class Motor:
    async def forward():
        Mot1a.value = True
        Mot1b.value = False
        Mot2a.value = False
        Mot2b.value = True

        await sleep(0.5)

        Mot1a.value = False
        Mot1b.value = False
        Mot2a.value = False
        Mot2b.value = False


    async def backward():
        Mot1a.value = False
        Mot1b.value = True
        Mot2a.value = True
        Mot2b.value = False

        await sleep(0.5)

        Mot1a.value = False
        Mot1b.value = False
        Mot2a.value = False
        Mot2b.value = False



    async def stop():
        Mot1a.value = False
        Mot1b.value = False
        Mot2a.value = False
        Mot2b.value = False

    async def turn_right():
        Mot1a.value = True
        Mot1b.value = False
        Mot2a.value = True
        Mot2b.value = False

        await sleep(0.5)

        Mot1a.value = False
        Mot1b.value = False
        Mot2a.value = False
        Mot2b.value = False

    async def turn_left():
        Mot1a.value = False
        Mot1b.value = True
        Mot2a.value = False
        Mot2b.value = True

        await sleep(0.5)

        Mot1a.value = False
        Mot1b.value = False
        Mot2a.value = False
        Mot2b.value = False



encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GP27, board.GP28, None,), # encoder #1 
    # reversed direction encoder with no button handling and divisor of 2
    (board.GP7, board.GP6, None,), # encoder #2
    )

keyboard.keymap = [
    [
    [KC.TO(2), KC.B, KC.MUTE],
    [KC.D, KC.E, KC.F]
    ],
    [
    [KC.TO(1), Motor.forward, KC.C],
    [Motor.turn_right, Motor.backward, Motor.turn_right]
    ],
]

encoder_handler.map = [ (( KC.VOLD, KC.VOLU, KC.MUTE), ( KC.VOLD, KC.VOLU, KC.MUTE), ), # Layer 1
                      ]


if __name__ == '__main__':
    keyboard.go()