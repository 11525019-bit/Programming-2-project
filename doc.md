# How the code works
## [__script.rpy__](https://github.com/11525019-bit/Programming-2-project/blob/main/game/script.rpy)
This file is where all the dialogs, images and sound appear when you play.

We will first create the characters and the story-teller's dialogue by the command: `define character_symbol = character("character_name", color = "color_code")`
```python
define l = Character("Luna", color = "#cb2915")
```
However, we don't want to show the story-teller's name so we will use this command instead:
```python
define n = Character(None)
```
Then, we will let Ren'py know that we are coding by Python so we use the command: `init:`
```python
init:
```
Next, we want to the character to appear on the screen so we generate the character images without the background so we can easily change the character's emotion and action by replacing character's images. We also do the same with the background images. To do so, firstly, we have to generate the images and put them in the image folder of the game. Then, we will define the images in the code by the command: `image image_name_in_game = "image_file"`
```python
image luna angry = "luna_angry.jpg"
```
For the sound effect, we will download the sound effect file and upload them in the sfx, bgm1, bgm2 folder then we insert them by using the command: `define sxf_name_in_game = "sfx_file"
```python
define sound_clothes   = "audio/sfx/sound_clothes.mp3"
```
However, in some sound effect file, we just want them to play in a specific period, we will add the time period before the sound effect file: `define sound_clothes   = "<from t1 to t2>audio/sfx/sound_clothes.mp3"`
```python
define sound_small_ppl   = "<from 1 to 10>audio/sfx/sound_small_ppl.mp3"
```
Then, we will import the chess library through this command:
```python
init 5 python:
    import_dir = os.path.join(renpy.config.gamedir, Chess_File, 'python-packages')
    global_objects = {}
```
The funtion of the `init 5 python` is to let Ren'py know that the following code is used in python with the priority level is 5
And the code `import_dir = os.path.join(renpy.config.gamedir, Chess_File, 'python-packages')` is to import the chess library
The last code `global_objects = {}` is used to store chess engine safely
Then we will devide the game in some sections in order to generate more than 1 endings for the game. We ultilize this command to do so: `label section_name:`
```python
label start:
```
In each section, we will add characters' dialogue, images and sound effect. For example, we will want to give the players specific endings based on how they respond to the character so we will give points to players for each choice then we will calculate the total point and give the endings to them. Therefore,we will, first, create the point system:
```python
$ point = Point()
```
Then, we will displace the backgrounds with the command: `scene background_name_in_game with transition_effect`
```python
scene room evening with dissolve
```
Similarly, we will displace the character's images with the similar command(a bit different): `show image_name_in_game at position with transition_effect`
```python
show luna angry at center with dissolve
```
For musics or sound effects, we will use 2 commands to play them: when we want them to play `play sound sfx_name_in_game volume sfx_volume` and when we them to stop `stop sound`
```python
play sound sound_walking_in_house volume 0.25

stop sound
```
And this is how we illustate the characters' dialogue: `character_symbol "speech"`
```python
m "So tired, I should go to sleep"
```
After that, when we want the players to decide what to respond to the character, we will use this command: `menu:` and the following command
```python
menu:
  "Check the phone":
      n "Messages. Notifications. Promotions."
      n "A thousand tiny attempts to touch you without ever reaching you."
      m "So many voices."
      m "None of them feel alive."
```
and if we want to give the point to the players, we will add this command inside the `menu` command: `$ point.add(amount)`
```python
menu:
  "Ask her to walk with you":
      m "Walk with me."

      show luna shy with dissolve
      l "W-Why?"
      m "I don't know."
      m "The street feels less empty if someone is beside me."

      l "That's a weak reason."
      m "It's the only real one."

      l "Ok. I'm accept that reason this time."
      show luna smile with dissolve
      $ point.add(20)
```
At the end of the start section, we will calculate the total point and then send the players to each ending based on the total point by using this command: `jump section_name`
```python
if point.total()<=40:
        jump bad_ending
    elif point.total()<=60:
        jump locked_ending
    elif point.total()<=80:
        jump dead_ending
    else:
        jump chess_ending
```
There is a special section that is __quit__, this section helps the player to quit the game after the endings with an important command
```python
window hide
```

_____________________________________________________________________________________________________________________________________________________

## [__chess_displayable.rpy__](https://github.com/11525019-bit/Programming-2-project/blob/main/00-chess-engine/chess_displayable.rpy)
This file is use to generate screen for a chess game and play on it.

We will first define the path of the file we are using.
- We define each part of each folder where the code have to go through to get the file.
```python
define Chess_File = '00-chess-engine/'
define Image_File = 'images/'
define Audio_File = 'audio/'
```
- Then add each step to get into the file location.
```python
define Chessboard_Image = Chess_File + Image_File + 'chessboard.png'
define Move_Audio = Chess_File + Audio_File + 'move.wav'
```

Then we will define the screen board size.
```python
define Screen_Width = 1280
define Screen_Height = 720
```



_____________________________________________________________________________________________________________________________________________________
## [__engine.rpy__](https://github.com/11525019-bit/Programming-2-project/blob/main/game/engine.rpy)
This engine is generated to give players points(affection points). 

We will, first, let Ren'py know that we are coding on python by using the same command as mentioned on the Script.rpy:
```python
init -5 python:
```
Then we create `class point` to administrate the point. In that class, we have 3 function, first is generating the point system, then we will write a function to add point to players, lastly, we will write a function to return the total point.
1. Generating point system:
We will define the function first:
```python
def __init__(self):
```
But we want the point to always start at 0 so we add a command to that funtion:
```python
self.affection = 0
```
2. Point adding function:
Similarly, the first thing to do is to define the function:
```python
def add(self, amount=10):
```
Then we will need a command to add point to the total point:
```python
self.affection = min(100, self.affection + amount)
```
However, we don't want the point to exceed 100 so `min(100, self.affection + amount)` is used to limit the total point.
3. Returning the total point function:
We will define the function and let the function return the total point:
```python
def total(self):
    return self.affection
```
