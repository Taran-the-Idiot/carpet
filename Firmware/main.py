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
from kmk.extensions.media_keys import MediaKeys



keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, holdtap, encoder_handler]

keyboard.col_pins = (board.GP0, board.GP1, board.GP4)
keyboard.row_pins = (board.GP5, board.GP3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

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
    [KC.NO, KC.TO(1), KC.NO],
    [KC.TO(1), KC.TO(2), KC.TO(3)]
    ], # Transfer layer - like use this to swap to other layers
    [
    [KC.TO(3), KC.MUTE, KC.TO(0)],
    [KC.MRWD, KC.MPLY, KC.MFFD]
    ], # Media layer - why is copilot trying to copy my writing style
    [
    [KC.MUTE, KC.LGUI(KC.X), KC.TO(0)],
    [KC.LGUI(KC.C), KC.LGUI(KC.V), KC.LGUI(KC.LSFT(KC.V))]
    ], # Cut/copy/paste/clean paste 
    [
    [KC.MUTE, KC.LGUI(KC.LSFT(KC.T)), KC.TO(0)],
    [KC.LGUI(KC.LSFT(KC.N4)), KC.LGUI(KC.LSFT(KC.R)), KC.LGUI(KC.LSFT(KC.W))]
    ], # Page stuff plus screenshot
    [
    [KC.MUTE, Motor.forward, KC.TO(0)],
    [Motor.turn_right, Motor.backward, Motor.turn_right]
    ], # driving layer
]

encoder_handler.map = [ 
    (( KC.VOLD, KC.VOLU), ( KC.BRIU, KC.BRID), ), # Layer 0
    (( KC.VOLD, KC.VOLU), ( KC.BRIU, KC.BRID), ), # Layer 1
    (( KC.VOLD, KC.VOLU), ( KC.BRIU, KC.BRID), ), # Layer 2
    (( KC.VOLD, KC.VOLU), ( KC.BRIU, KC.BRID), ), # Layer 3
    ]


if __name__ == '__main__':
    keyboard.go()