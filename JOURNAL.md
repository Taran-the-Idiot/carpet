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

![bleh](https://cdn.hackclub.com/019dec72-22fd-77ca-a92e-7cd679c9228d/Screen%20Shot%202026-05-02%20at%2011.00.14%20pm.png)

imported a servo model into the cad. and lowkey, its pretty big. like really big. and das not very sigmer. so liek, i should probably change that.

Mr nimit told me to use an n20 motor cuz those are small, so thats what I did.

the pcb will stay the same shape so I dont really need to swap that out but I will still need to add in a transistor and change that stuff up a bit. however thats a problem for future me, not now me.

![bleh](https://cdn.hackclub.com/019decac-f3db-7ab8-8144-6e69fe917990/Screen%20Shot%202026-05-02%20at%2011.43.10%20pm.png)

N20 motors placed

![here](https://cdn.hackclub.com/019decad-3c95-7f5d-99e3-e285956d95ae/Screen%20Shot%202026-05-02%20at%2011.43.20%20pm.png)

Here is what it looks like on the bottom, I might thin out the walls where the motors are so they can have more shaft sticking out.

![bazinga](https://cdn.hackclub.com/019decae-92b6-7ea2-8d1f-5fc72fbc719c/Screen%20Shot%202026-05-02%20at%2011.44.39%20pm.png)

Extend walls


![extend downwards](https://cdn.hackclub.com/019decae-df5d-7b03-aeb2-cae23c0c1af1/Screen%20Shot%202026-05-02%20at%2011.50.20%20pm.png)

extend downwards and make a hole where the shaft is. the hole is 6mm diameter while the shaft has a 3mm diameter. this way it has wiggle room and room for me to make mistakes.

![motoa](https://cdn.hackclub.com/019decb0-9d72-77be-9bd4-05ff350ce7fa/Screen%20Shot%202026-05-02%20at%2011.50.30%20pm.png)

Here is what it looks like with the motors in. I will need to make a mount for the motors. I dont wanna just hot glue them.

![brotato](https://cdn.hackclub.com/019ded64-df01-71b8-a335-8170dbb81fb2/Screen%20Shot%202026-05-02%20at%2011.55.30%20pm.png)

wheel. it is being made. wheel go wheel and wheel go spin.

![image](https://cdn.hackclub.com/019deda2-78e9-7c22-b6f7-84fca705649a/Screen%20Shot%202026-05-03%20at%2012.07.51%20am.png)

Gave it triangular cutout thingies to reduce weight and stuff(lies its cuz it looks cool)

Also gave it an indent in the middle. will use that indent to either put a bunch of rubber bands or have a tpu insert for grip cuz pla aint gonna cut it

![phil](https://cdn.hackclub.com/019deda8-35a9-7707-bd0e-e41fb58942c5/Screen%20Shot%202026-05-03%20at%2012.11.17%20am.png)

a little fillet goes a long way

![fill](https://cdn.hackclub.com/019dede8-7ef7-7c41-84b9-1cc118f3a0ef/Screen%20Shot%202026-05-03%20at%2012.21.50%20am.png)

added a lot more fillets. this is done for now but im not 100% happy with how it turned out so expect a redesign in the future.

Time spent: 2 hours 30 mins

## 3rd of May 

Didnt do too much today

![image](https://cdn.hackclub.com/019dede9-7d4f-7593-893a-78ba167fad13/Screen%20Shot%202026-05-03%20at%209.26.32%20pm.png)

I just narrowed down the hole for the encoder

I also did a bit of research and found out that the n20 motors have no real mounting holes. meaning I will be infact hot glueing this to the case. but I will also probably have a sandwich with some screws there for the main holding mech.

![made these for the motors](https://cdn.hackclub.com/019dee04-c4ad-7115-a425-c673fe4eb62a/Screen%20Shot%202026-05-03%20at%2011.26.01%20pm.png)

made these for the motors. its cool and holds them in place

![potato](https://cdn.hackclub.com/019dee0e-9b3e-7333-89e4-d6d594a90114/Screen%20Shot%202026-05-03%20at%2011.36.46%20pm.png)

Now I added these to cover the top. will add screw holes in later but the plan is to have these in with hot glue and then also screwed in with the brace. I also need to figure out how to get the wires around the big thing I made so will also need to figure that out

But those are problems for tomorrow 

Time spent: 30 mins


