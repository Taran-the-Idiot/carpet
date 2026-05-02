# A Macropad, that drives????

## 2nd of May

Insert sketch here

Tldr: macropad but give it wheels and make it drive

How? probably just continous rotation servos and stuff

Why? idk its funny

Anyways time to make schematic

Okay I got sidetracked by stinky tiktik but starting now at 8:10

first things first i need a microcontrolelr. im not fixing that spelling mistake screw you.

lowkirkuinely might just get a xiao rp2040. its cheapish and works.

the rest is just gonna be 2 servos and some switches, maybe an encoder

![imag](https://cdn.hackclub.com/019de838-f7f6-7f5f-bd3c-65518c793d9c/Screen%20Shot%202026-05-02%20at%208.25.04%20pm.png)

parts placed :)

2 encoders cuz encoders are cool, then 4 switches and 2 servos. its gonna be continous rotation servos and not a 270 degree one so it can actually drive. might add a sensor or smth to give it pid but thats a problem for future me to decide.

Okay so i made most of the connections on the schamatic, and I perfectly used every pin

![img](https://cdn.hackclub.com/019de851-80b4-76ed-9e8d-cfe0b5f3ac5c/Screen%20Shot%202026-05-02%20at%208.49.31%20pm.png)

ts so peak.

100% intentional frfr

anyways now time to find some continous rotation servos so i can find voltage

[link](https://www.aliexpress.com/item/1005007614288642.html?src=google&src=google&albch=shopping&acnt=179-224-6891&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=_oFgTQeV&gclsrc=aw.ds&albagn=888888&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=en1005007614288642&ds_e_product_merchant_id=5404900884&ds_e_product_country=AU&ds_e_product_language=en&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=23105125349&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gad_campaignid=23099558562&gbraid=0AAAABBR8xIctleUnkzkTs3F-kQ-hWbXae&gclid=CjwKCAjwwdbPBhBgEiwAxBRA4a2Bmfq_W-Cp04UZTLLzow1ql5YwxvVK6J7bNR_aAUIHiwYXpFfLPRoC9CUQAvD_BwE#nav-specification)

bazinga

this thingy says I need 4.8-6V so imma hook it up to 5V

![image](https://cdn.hackclub.com/019de853-5db3-7fbf-aea4-c3a601ca6398/Screen%20Shot%202026-05-02%20at%208.54.19%20pm.png)

Huzzah

![banana](https://cdn.hackclub.com/019de887-27a6-76f7-96f8-3d006521b36f/Screen%20Shot%202026-05-02%20at%209.09.37%20pm.png)

Schematic before routing looks like this. its cool ig not much to tlak about

![bleh](https://cdn.hackclub.com/019de887-d76e-7b9c-9eb9-e0d8c7285bef/Screen%20Shot%202026-05-02%20at%209.09.42%20pm.png)

here is the footprint assignments


onwards to pcb bullshittery

![parts](https://cdn.hackclub.com/019de888-747a-76a2-ab5d-5265bf7cf7cc/Screen%20Shot%202026-05-02%20at%209.15.19%20pm.png)

Placed ma parts down. Tried to go for a compactish build(also started routing a bit but thats cuz i forgor to take the ss earlier)


![routing](https://cdn.hackclub.com/019de889-688c-7120-a637-2afd509bdbb1/Screen%20Shot%202026-05-02%20at%209.24.34%20pm.png)

routing yay

Aslso moved arounf the headers for the servos off a bit closer to the microcontroller. probably wont use headers for the real build anyways but imma leave them in for now.


![cutlines](https://cdn.hackclub.com/019de88b-1ca4-7d2a-a0cd-71e07fa98330/Screen%20Shot%202026-05-02%20at%209.26.06%20pm.png)

added cutlines. plus gave them routed corners. I also used the inbuilt fuction thingy that kicad has for filleting corners. first time using it too. but its a bit funny working when you try to fillet individual lines.

![model](https://cdn.hackclub.com/019de88c-7024-7e5d-a20a-a81a15928f9e/Screen%20Shot%202026-05-02%20at%209.28.18%20pm.png)
 
model generated

![mdel2](https://cdn.hackclub.com/019de88c-c632-7351-bc84-0501af29a4d1/Screen%20Shot%202026-05-02%20at%209.39.18%20pm.png)

Found some models for the parts missing models and now finished model(the servos will be in the build cad cuz its gonna be case reliant)

Potato

![banan](https://cdn.hackclub.com/019de88d-99a8-74dc-9be6-9e1a3ada060a/Screen%20Shot%202026-05-02%20at%209.50.56%20pm.png)

Here is my finished schematic cuz I needed to change around some of the pin locations since im dum and routing got annoying

okay time to go to cad

Silkscreen stuff imma do later, not bothered rn

Time spent: 1.5 hours (90 mins)


## May 2nd(again)

Splitting this into its own entry cuz like idk shorter entries or smth

![plate](https://cdn.hackclub.com/019de89c-62bb-7905-a704-71eff388bc7f/Screen%20Shot%202026-05-02%20at%2010.10.48%20pm.png)

plate

not much to it. its 3mm thick

![blhe](https://cdn.hackclub.com/019de89c-be33-7f8d-b9c9-e4b7cf9a78ce/Screen%20Shot%202026-05-02%20at%2010.12.31%20pm.png)

added the relief cuts/space for it to click/whatever you call em.

since mx switches need 1.5mm plates, and I used 3mm plate, i made a 0.5mm cut on the bottom 1.5mm of the plate so it like allows it to click in instead of friction fit


imma write it tmrw, not bothered rn

Time spent: 2 hours 30 mins

