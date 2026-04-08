# How the code work (part 2)
## [__chess_displayable.rpy__](https://github.com/11525019-bit/Programming-2-project/blob/main/00-chess-engine/chess_displayable.rpy)
This file is use to generate screen for a chess game and play on it.

### __Define__
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

After that, we will define the chess board size.
```python
define Board_Size = Screen_Height
```

Because the board size is 720 and each side of the board has 8 square so the square length is 90 so we define the square length equals to 90.
```python
define Loc_Legth = 90
```

Next, we will name the columns with letters and rows with numbers.
```python
define Index_Min = 0
define Index_Max = 7
define File_Letters = ('a','b','c','d','e','f','g','h')
```

Then, we will define the promotion of pawns when white pawns reach the last row and black pawns reach the first row. When the pawn reach that rank, the pawn is one move away to promote so the code will detect it, that why it is 6 ```7-1``` and 1 ```0+1```.
```python
define Promotion_White = 6
define Promotion_Black = 1
```

After that, we will define the color of the hover, the selected square, the legal move square, the previous move square and the white squares.
```python
define Hover_Color = '#90ee90aa' # HTML LightGreen
define Selected_Color = '#40e0d0aa' # Turquoise
define Legal_DST_Color = '#afeeeeaa' # PaleTurquoise
define Previous_Move_Color = '#6a5acdaa' # SlateBlue
define White_Color = '#fff'
```

Next, we can define the visual scale with the layout offsets of the board as an UI.
```python
define Text_Size = 26
define Text_Button_Size = 45 # promotion piece and flip-board arrow button
define Text_Whose_Turn_Coordinate = (-260, 40)
define Text_Status_Coordinate = (-260, 80)
```


```python

```


```python

```
