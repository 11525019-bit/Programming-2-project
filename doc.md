# How the code works
We will first create the characters and the story-teller's dialogue by the command: `define character_symbol = character("character_name", color = "color_code")`
```python
define l = Character("Luna", color = "#cb2915")
```
However, we don't want to show the story-teller's name so we will use this command instead:
```python
define n = Character(None)
```
Next, we want to the character to appear on the screen so we generate the character images without the background so we can easily change the character's emotion and action by replacing character's images. We also do the same with the background images. To do so, firstly, we have to generate the images and put them in the image folder of the game. Then, we will define the images in the code by the command: `image image_name_in_code = Image("image_file")`
```python
image luna angry = Image("luna_angry.jpg")
```
