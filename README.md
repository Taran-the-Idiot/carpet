![image](https://cdn.hackclub.com/019e6412-3a0e-7e8a-ade5-07bf7a9bccb4/render2.png)

# Driving Macropad

What if you had a macropad, that drives????

This is your average macropad by day but with the push of a button it turns into a toy car you can drive around on your desk. It has 4 cherry MX switches and 2 EC11 rotary encoders. For the drive motors it uses 2 N20 motors

It runs off a custom made RP2040 dev board and uses kmk firmware.


## PCB

![imge](https://cdn.hackclub.com/019e63ff-f0b9-7a0e-ba84-3cf6746752c1/paste-1779794174969.png)

### Schematic

![image](https://cdn.hackclub.com/019e640a-167a-7691-ac02-ec3acb2c085b/Screen%20Shot%202026-05-26%20at%209.17.20%20pm.png)

This board runs on a [custom devboard](https://github.com/Taran-the-Idiot/Taranium-RP2040) that was built for this use case. 

The motors used for the drive system are N20 motors and they are powered using the L293D motor controlelr.

For the macropad side of things, this board uses a 2x3 matrix with 4 MX keys and 2 encoders. 

In order to preserve size and packaging, a choice was made to avoid using a battery and instead the pad is run off of cable power direct from usb. 


### PCB Top Side

![image](https://cdn.hackclub.com/019e640c-2eb4-79d8-888c-5e0cd09cc771/Screen%20Shot%202026-05-26%20at%209.28.56%20pm.png)

### PCB Bottom Side

![image](https://cdn.hackclub.com/019e640c-7550-7a46-b829-eb981d8346a8/Screen%20Shot%202026-05-26%20at%209.29.20%20pm.png)



## CAD

![image](https://cdn.hackclub.com/019e6ebf-0731-7213-8422-03ac1d460ef5/render2.png)

CAD Was made in Shapr3d. It is your basic macropad case but also includes 2 wheels that go directly on the motor shafts and are lined with TPU treads for grip.

THe 2 holes on the top of the case exist for the purpose of being able to reach the boot and reset buttons on the microcontroller without having to break open the case.

There are 2 fake wheels on the lower section that exist for the purpose of reducing friction between the pad and the desk due to the lower surface area.



## Firmware

This board uses KMK as the driving software for its functionality.

The board has 5 layers in the following format:

- Layer Swap - Used to pick the layer you wish to use
- Audio/Music Control - Used to control your music player
- Keyboard Commands - Commonly used keyboard commands
- Page Controls - Keyboard commands to open/close web pages
- Drive Control - Control how the pad drives


On the driving aspect, you can call the following functions in order to allow the pad to drive:


`forward()` - Move the pad forward\
`backward()` - Move the pad backward\
`turn_right()` - Turn the pad right\
`turn_left()` - Turn the pad left\
`stop()` - Stops both motors

Currently the functions are not tuned to specific degree turns or specific distances.\
However that would more than likely depend and differ between builds so I recommend tuning them yourself anyways to get the desired outcomes.


## BOM


