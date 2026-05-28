# A Macropad, that drives????

Total time spent: 18.5 hours

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

## 4th of May

So uhhh I kinda forgot to take screenshots of this part but I made the bottom floor, added treads to the tires, and made a top for the microcontroller section. but anyways I got stuck on what to add after that. So what to do so I went back to the pcb to convert it from using servos to using motors. 

After that I reached a big problem. I ran out of pins. since h bridge motor drivers use 2 pins to drive them instead of 1, I need 2 pins that do not exist on my microcontroller. 

After a bit of searching for a potential replacement that has enough pins, I couldn't find anything. so kill me ig. I might just go and make my own. off on a sidequest ig.

Hours spent: 3

(probably spent more but cant remember so putting the bare minimum I would have realistically spent)

## 19th of May

Reterneth I haveth

![image](https://cdn.hackclub.com/019e67de-d4ba-7fc2-abc6-4087cc70846b/Screen%20Shot%202026-05-19%20at%2011.19.44%20pm.png)


New microcontroller has been made and has been inserted into boardeth. okay the eths are getting annoying now

![image](https://cdn.hackclub.com/019e67df-8d20-72ce-acd4-3bb9cd1af024/Screen%20Shot%202026-05-19%20at%2011.19.50%20pm.png)

Pins. assigned like this. 

Thats it for today

Time spent: 10 mins or smth

## 21st of may


![image](https://cdn.hackclub.com/019e67e0-11f4-768d-a6a1-1278efe7a63e/Screen%20Shot%202026-05-21%20at%201.16.27%20pm.png)

after some back and forth research about good h bridges and stuff, I landed on the L293D cuz everyone just universally says that its good. And i am a sheep that trusts the masses so the L293D is good h bridge that I shall be using

![image](https://cdn.hackclub.com/019e67e0-6797-78cc-95d0-0e65c48465c0/Screen%20Shot%202026-05-21%20at%201.16.32%20pm.png)

Anyways wired like so


![image](https://cdn.hackclub.com/019e67e1-e985-7e3a-94fe-05c8bd8b0250/Screen%20Shot%202026-05-21%20at%201.31.10%20pm.png)


I Assigned the pins like so for now, will probably need to change them

![image](https://cdn.hackclub.com/019e67e2-6c01-79fc-ac9e-30ee0b131dcb/Screen%20Shot%202026-05-21%20at%201.31.17%20pm.png)

placed the parts and routed the l293d and the power lines. the other lines need their assignments swapped aroind


![image](https://cdn.hackclub.com/019e67e4-0b18-799c-9c73-41968ce7a09a/Screen%20Shot%202026-05-21%20at%201.32.07%20pm.png)


here is what i landed with


![image](https://cdn.hackclub.com/019e67e4-4938-7b32-a7c7-3c50f6aa1098/Screen%20Shot%202026-05-21%20at%201.33.35%20pm.png)

I then moved it a bit cus those pins were closer and I dont want to take the traces on a huge journey across the world(or in this case, further down the street)

![image](https://cdn.hackclub.com/019e67e7-457f-79ad-b60b-9c027e865b4e/Screen%20Shot%202026-05-21%20at%201.52.26%20pm.png)

I am using a normal fill on the front and a hatch on the back. and I discovered that if you put vias on a hatch fill, it makes this cool pattern. 

except it looks weird if you dont have all the vias fully centred. and I AM NOT gonna be sitting here placing perfect vias on like 200 points.


![image](https://cdn.hackclub.com/019e67e8-da54-7759-86d6-f199b2c8386f/Screen%20Shot%202026-05-21%20at%201.56.04%20pm.png)

I WILL however be putting down my amongus vias down in the corner over there


![image](https://cdn.hackclub.com/019e67e9-7911-7bcd-afd2-50fd2bd4830e/Screen%20Shot%202026-05-22%20at%208.42.37%20am.png)

pcb be looking fine af. I still need silkscreen but thats a problem for future me, not now me.

Hours spent: 3



## 26th of May

Made stuff

![image](https://cdn.hackclub.com/019e6dc3-3d59-745c-b7fd-47230abf25e4/Screen%20Shot%202026-05-26%20at%2011.03.32%20am.png)


Added the pcb and adjusted the size of the case to fit it. Cuz the old microcontroller was shorter so case adjustment needed. It only really just needed a cut and some extrusion and remerge. not too bad


![image](https://cdn.hackclub.com/019e6dd3-0c97-7f34-abf9-ce64fe1f30d4/Screen%20Shot%202026-05-26%20at%2011.08.08%20am.png)

I adjusted the position of the motor wire holes because they were slightly misaligned with the slots I made in the case.

![image](https://cdn.hackclub.com/019e6dd3-ca8f-7668-a50a-0e6716cc0827/Screen%20Shot%202026-05-26%20at%2012.52.02%20pm.png)

Okay this thing was annoying af. I spent like 30 minutes trying to figure out why it wouldnt union with the rest of the case. And after some back and forth between google, I imported it into onshape and tried it and it told me that it basically is illegal to merge the 2 since I made a body have  join at the edge and it needs some kind of full connection or else the file will kill itself



![image](https://cdn.hackclub.com/019e6dd5-e946-7a30-bf6e-f79aa3a70c6d/Screen%20Shot%202026-05-26%20at%204.18.15%20pm.png)

![image](https://cdn.hackclub.com/019e6dd5-84b8-7e07-866c-01bbd021b92c/Screen%20Shot%202026-05-26%20at%2012.57.51%20pm.png)

Made a cutout for the usbc plus extra room for the cable

![image](https://cdn.hackclub.com/019e6dd6-53a4-7bf2-8cfb-9d62072d3334/Screen%20Shot%202026-05-26%20at%205.06.42%20pm.png)


Added a border around the switches to half hide the stems and half make it look better cuz i dont like it when its not contained.


![image](https://cdn.hackclub.com/019e6dd7-84b1-716c-8965-2d19f4a5e5e7/Screen%20Shot%202026-05-26%20at%205.30.43%20pm.png)

the gray was pissing me off so i went and made everything red again

![image](https://cdn.hackclub.com/019e6dd8-06e7-7baf-bbe5-756eda93ce43/Screen%20Shot%202026-05-26%20at%205.59.18%20pm.png)

this was clipping

![image](https://cdn.hackclub.com/019e6dd8-691a-7fb0-a823-5d1f6ab36ec1/Screen%20Shot%202026-05-26%20at%206.00.36%20pm.png)

so i went and rounded out the bottoms of the knobs so it dont clip anymore


![image](https://cdn.hackclub.com/019e6dd8-e325-77e4-8a68-5801c5eb098c/Screen%20Shot%202026-05-26%20at%206.00.56%20pm.png)

looks yummy

![image](https://cdn.hackclub.com/019e6dd9-5e14-72bd-b3d5-2e2ba1cf4d9a/Screen%20Shot%202026-05-26%20at%206.23.11%20pm.png)

added holes mainly to be able to access the boot button and the reset button since I learn from my mistakes and am not gonna remove my access to them again.


![image](https://cdn.hackclub.com/019e6dda-2afb-78e5-a779-9fd680c31f8a/Screen%20Shot%202026-05-26%20at%206.45.50%20pm.png)


tried to make it blend in better and be more non-chanlant but lowkey looks like dog doo-doo.


![image](https://cdn.hackclub.com/019e6df2-f6cd-7d8c-8278-076c3e3df8fa/Screen%20Shot%202026-05-26%20at%207.31.33%20pm.png)

I moved on the the botton and made the 2 motor covers into 1 piece so its less finicky and also covers up the space at the bottom

![image](https://cdn.hackclub.com/019e6df3-bc8f-7cf5-8197-3a8b0c1161fe/Screen%20Shot%202026-05-26%20at%207.31.40%20pm.png)

also wanna close that gap there


![image](https://cdn.hackclub.com/019e6df4-2b37-7cda-aaa7-17435798af8f/Screen%20Shot%202026-05-26%20at%207.34.00%20pm.png)

gap has been closed plus gave a small amount of clearance cuz i dont care about an airtight seal

![image](https://cdn.hackclub.com/019e6df4-c50e-791b-8e61-cd3ae9e8a2f9/Screen%20Shot%202026-05-26%20at%208.06.29%20pm.png)


I think i have finally lost my sense for design. my older projects have always been way better than this

![image](https://cdn.hackclub.com/019e6e16-8a00-7b62-873e-dc085c0742f6/Screen%20Shot%202026-05-26%20at%208.14.28%20pm.png)

i simplified it down back to these 2 holes and i lowkenuienly have no clue how to do this and make it look good.

![image](https://cdn.hackclub.com/019e6e1e-135f-7921-9741-d0b02e982ab9/Screen%20Shot%202026-05-26%20at%208.33.44%20pm.png)

i give up. we engrave potato on it

![image](https://cdn.hackclub.com/019e6e22-0c52-742b-80c3-ab167ab5e114/Screen%20Shot%202026-05-26%20at%208.38.51%20pm.png)


put website link here and also put my logo on the bottom of the case


![image](https://cdn.hackclub.com/019e6e2c-652d-78a0-9ddb-88e17e3c4834/Screen%20Shot%202026-05-26%20at%208.57.19%20pm.png)


silkscreen. im trying to do a thing

![image](https://cdn.hackclub.com/019e6e2c-b3e5-7e71-835c-a5f46073a527/Screen%20Shot%202026-05-26%20at%208.59.51%20pm.png)

okay it may look sucky but trust the process frfr. it only looks bad now cuz its deisgn file and most of it will get ut off.


![image](https://cdn.hackclub.com/019e6e2d-5ea4-787c-946b-4f983f400652/Screen%20Shot%202026-05-26%20at%209.08.39%20pm.png)

tada. its a bit wonky but we can work with it and lowkey looks nice.




![image](https://cdn.hackclub.com/019e6e2e-3595-7ad1-81ca-c4132859d5a9/render2.png)


renda of the final product.

Hours Spent: 7


## 27th of May

Wrote the firmware. 

I used kmk for this and it was pretty easy. Gave it 4 layers and wrote custom functions for the driving. will probably make it more complex later once I get the thing and am able to tinker but this works technically.

Hours spent: 1




