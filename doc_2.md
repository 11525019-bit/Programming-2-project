# How the code work (part 2)
## [__chess_displayable.rpy__](https://github.com/11525019-bit/Programming-2-project/blob/main/00-chess-engine/chess_displayable.rpy)
This file is use to generate screen for a chess game and play on it.

### Table of Contents
- [Define](https://github.com/11525019-bit/Programming-2-project/blob/main/doc_2.md#define)
- [Style](https://github.com/11525019-bit/Programming-2-project/blob/main/doc_2.md#style)
- [Screen](https://github.com/11525019-bit/Programming-2-project/blob/main/doc_2.md#screen)
  - [Game Status](https://github.com/11525019-bit/Programming-2-project/blob/main/doc_2.md#left-top-panel--game-status)
  - [Controls](https://github.com/11525019-bit/Programming-2-project/blob/main/doc_2.md#left-bottom-panel--controls)
  - [The Chess Board](https://github.com/11525019-bit/Programming-2-project/blob/main/doc_2.md#middle-panel--the-chess-board)
  - [Promotion UI](https://github.com/11525019-bit/Programming-2-project/blob/main/doc_2.md#right-panel--promotion-ui)
- [Python Classes](https://github.com/11525019-bit/Programming-2-project/blob/main/doc_2.md#python-classes)
  - [Hover Displayable](https://github.com/11525019-bit/Programming-2-project/blob/main/doc_2.md#hoverdisplayable)
  - [Chess Displayable](https://github.com/11525019-bit/Programming-2-project/blob/main/doc_2.md#chessdisplayable)
  - [Helper Methods](https://github.com/11525019-bit/Programming-2-project/blob/main/doc_2.md#helper-methods)
- [Helper Functions](https://github.com/11525019-bit/Programming-2-project/blob/main/doc_2.md#helper-functions)


### __Define__

We will first define the path of the file we are using.

```python
define Chess_File = '00-chess-engine/'
define Image_File = 'images/'
define Audio_File = 'audio/'
```
We define each part of each folder where the code has to go through to get the file.

```python
define Chessboard_Image = Chess_File + Image_File + 'chessboard.png'
define Move_Audio = Chess_File + Audio_File + 'move.wav'
```
Then add each step to get into the file location.

```python
define Screen_Width = 1280
define Screen_Height = 720
```
Then we will define the screen board size.

```python
define Board_Size = Screen_Height
```
After that, we will define the chess board size.

```python
define Loc_Legth = 90
```
Because the board size is 720 and each side of the board has 8 squares, the square length is 90, so we define the square length equal to 90.

```python
define Index_Min = 0
define Index_Max = 7
define File_Letters = ('a','b','c','d','e','f','g','h')
```
Next, we will name the columns with letters and rows with numbers.

```python
define Promotion_White = 6
define Promotion_Black = 1
```
Then, we will define the promotion rank for pawns. When the white pawn reaches rank index 6 (`7-1`), it is one move away from promoting — the code detects this to show the promotion UI. Same logic applies for the black pawn at rank index 1 (`0+1`).

```python
define Hover_Color = '#90ee90aa'       # HTML LightGreen  — square the cursor is hovering over
define Selected_Color = '#40e0d0aa'    # Turquoise        — square the player has clicked/selected
define Legal_DST_Color = '#afeeeeaa'   # PaleTurquoise    — squares the selected piece can legally move to
define Previous_Move_Color = '#6a5acdaa' # SlateBlue      — the two squares involved in the last move
define White_Color = '#fff'            # White            — used for text labels
```
After that, we will define the highlight colors used on the board. Each color uses an RGBA hex code where the last two characters (`aa`) control transparency.

```python
define Text_Size = 26                               # font size for status text (e.g. "Whose turn")
define Text_Button_Size = 45                        # font size for promotion piece buttons and flip-board button
define Text_Whose_Turn_Coordinate = (-260, 40)      # position offset for the "whose turn" label
define Text_Status_Coordinate = (-260, 80)          # position offset for the game status label (check, checkmate, etc.)
```
Next, we define the visual scale with the text sizes and layout coordinates for UI labels on the board panel.

```python
define Piece_Types = ('p', 'r', 'b', 'n', 'k', 'q')
```
Define what letters represent each piece type. Lowercase letters are used as keys to build the piece image filenames — uppercase will represent white pieces and lowercase will represent black pieces in python-chess.

```python
define Number_History = 5
```
Define how many past moves to display in the move history panel on the left side of the screen.

```python
define Min_Depth = 1
define Max_Depth = 20
```
Define the minimum and maximum search depth for the Stockfish AI. A higher depth means the AI looks further ahead but takes longer to compute.

```python
define Start_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
```
Define the starting board position using FEN notation (Forsyth–Edwards Notation), which is a standard way to describe a chess board state as a single string.
 
```python
define When_Checked = 1   # the current player's king is in check
define Threefold   = 2    # the same position has occurred three times (draw can be claimed)
define Fifty_Moves = 3    # fifty moves have passed with no capture or pawn move (draw can be claimed)
define Draw        = 4    # the game ended in a draw (stalemate, resign, or claimed)
define Checkmate   = 5    # the current player's king has been checkmated
define Stalemate   = 6    # the current player has no legal moves but is not in check
```
Finally, define the status code enum used throughout the game to represent the current game state. These integer constants make the code more readable than using raw numbers.

___________________________________________________________________________________________________________________________________________________________________________________________________________________________

## __Style__

Styles define the visual appearance of UI elements such as text labels and buttons.
```python
style game_status_text is text:
    font 'DejaVuSans.ttf'
    color White_Color
    size Text_Size
```
`game_status_text` is used for labels like "Whose turn: White" and "In Check". It uses a white font at the standard text size.

```python
style promotion_piece is button
style promotion_piece_text is text:
    font 'DejaVuSans.ttf'
    size Text_Button_Size
    color '#aaaaaa'         # gray when not interacted with
    hover_color '#555555'   # darker gray on hover
    selected_color White_Color  # white when selected
```
`promotion_piece` styles the four promotion buttons (rook, bishop, knight, queen) that appear when a pawn is about to promote. The text changes color depending on interaction state.

```python
style control_button is button
style control_button_text is text:
    font 'DejaVuSans.ttf'
    size Text_Button_Size
    color '#aaaaaa'         # gray by default
    hover_color White_Color # white on hover
```
`control_button` styles the resign (`⚐`) and flip board (`↑↓`) buttons. It turns white on hover to signal interactivity.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

## __Screen__

The `chess` screen is the main game screen. It is declared as `modal True`, which means it blocks all input to anything rendered behind it.

```python
screen chess(fen, player_color, depth):
    modal True
```

It accepts three parameters:
- `fen` — the starting board state in FEN notation.
- `player_color` — `chess.WHITE`, `chess.BLACK`, or `None` for Player vs. Player.
- `depth` — the Stockfish search depth.

Two default displayables are created when the screen loads:

```python
    default hover_displayable = HoverDisplayable()
    default chess_displayable = ChessDisplayable(
        fen=fen,
        player_color=player_color,
        depth=depth
    )
```

`HoverDisplayable` handles the green hover highlight. `ChessDisplayable` is the main game logic and rendering object.

### Left Top Panel — Game Status

```python
    fixed xpos 20 ypos 80 spacing 40:
        vbox:
            showif chess_displayable.whose_turn == chess.WHITE:
                text 'Whose turn: White' style 'game_status_text'
            else:
                text 'Whose turn: Black' style 'game_status_text'
```
This panel is pinned to the top-left. It shows whose turn it currently is by checking `whose_turn` on the displayable.

```python
            showif chess_displayable.game_status == Checkmate:
                text 'Checkmate' style 'game_status_text'
            elif chess_displayable.game_status == Stalemate:
                text 'Stalemate' style 'game_status_text'
            elif chess_displayable.game_status == When_Checked:
                text 'In Check' style 'game_status_text'
```
Below the turn label, the current game status is shown if applicable. Note that Draw and Resign are not displayed here because those conditions return immediately from the screen.

```python
            text 'Most recent moves' style 'game_status_text' xalign 0.5
            for move in chess_displayable.history:
                text move.uci() style 'game_status_text' xalign 0.5
```
This loops through the move history deque and displays each move in UCI format (e.g., `e2e4`). Up to `Number_History` (5) moves are shown.

### Left Bottom Panel — Controls

```python
    fixed xpos 20 ypos 500:
        vbox:
            hbox spacing 5:
                text 'Resign' color White_Color yalign 0.5
                textbutton '⚐':
                    action [Confirm('Would you like to resign?',
                        yes=[
                        Play('sound', Draw_Audio),
                        Return(not chess_displayable.whose_turn)
                        ])]
                    style 'control_button' yalign 0.5
```
The resign button opens a confirmation dialog. If confirmed, it plays the draw sound and returns the *opposite* of `whose_turn` — because the resigning player loses, so their opponent wins.

```python
            hbox spacing 5:
                text 'Flip board view' color White_Color yalign 0.5
                textbutton '↑↓':
                    action [Play('sound', Flip_Board_Audio),
                    ToggleField(chess_displayable, 'bottom_color'),
                    SetField(chess_displayable, 'has_flipped_board', True)]
                    style 'control_button' yalign 0.5
```
The flip board button plays a sound, toggles which color is displayed at the bottom of the board, and sets a flag so the displayable can reset any in-progress piece selection.

### Middle Panel — The Chess Board

```python
    fixed xpos 280:
        add Image(Chessboard_Image)
        add chess_displayable
        add hover_displayable
```
The board image is drawn first as the background, then `chess_displayable` renders pieces and highlights on top, then `hover_displayable` renders the green hover square on top of everything.

```python
        if chess_displayable.game_status == Checkmate:
            timer 4.0 action [Return(chess_displayable.winner)]
        elif chess_displayable.game_status == Stalemate:
            timer 4.0 action [Return(Draw)]
```
When the game ends in checkmate or stalemate, a 4-second timer fires and returns the result to the calling script. The delay lets the player see the final board position before the screen closes.

### Right Panel — Promotion UI

```python
    showif chess_displayable.show_promotion_ui:
        text 'Select promotion piece type' xpos 1010 ypos 180 color White_Color size 18
        vbox xalign 0.9 yalign 0.5 spacing 20:
            null height 40
            textbutton '♜':
                action SetField(chess_displayable, 'promotion', chess.ROOK) style 'promotion_piece'
            textbutton '♝':
                action SetField(chess_displayable, 'promotion', chess.BISHOP) style 'promotion_piece'
            textbutton '♞':
                action SetField(chess_displayable, 'promotion', chess.KNIGHT) style 'promotion_piece'
            textbutton '♛':
                action SetField(chess_displayable, 'promotion', chess.QUEEN) style 'promotion_piece'
```
This panel only appears when `show_promotion_ui` is `True`, which happens when the selected pawn is one step from the back rank. Clicking a button sets `chess_displayable.promotion` to the chosen piece type, which is then used when constructing the move.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

## __Python Classes__

The `init python:` block runs once at startup and defines all classes and helper functions.

It begins by importing the required libraries and setting up the Stockfish binary path based on the operating system:

```python
import os, sys, pygame
from collections import deque

import chess
import chess.engine
import subprocess
```

The correct Stockfish binary is chosen based on the platform (`renpy.android`, `renpy.windows`, etc.), and on Windows, `STARTUPINFO` is configured to prevent a terminal popup from appearing when the engine subprocess launches.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

### HoverDisplayable

`HoverDisplayable` is a lightweight displayable that only draws one thing: a green square under the mouse cursor.

```python
class HoverDisplayable(renpy.Displayable):
    def __init__(self):
        super(HoverDisplayable, self).__init__()
        self.hover_coord = None
        self.hover_img = Solid(Hover_Color, xsize=Loc_Legth, ysize=Loc_Legth)
```
`hover_coord` stores the rounded screen coordinate of the current mouse position. `hover_img` is a pre-built solid green square.

```python
    def render(self, width, height, st, at):
        render = renpy.Render(width, height)
        if self.hover_coord:
            render.place(self.hover_img,
                x=self.hover_coord[0], y=self.hover_coord[1],
                width=Loc_Legth, height=Loc_Legth)
        return render
```
`render` is called every frame. It draws the green square at `hover_coord` if the mouse is over the board. If the mouse is outside the board, `hover_coord` remains `None` and nothing is drawn.

```python
    def event(self, ev, x, y, st):
        if 0 < x < Board_Size and 0 < y < Board_Size and ev.type == pygame.MOUSEMOTION:
            self.hover_coord = round_coord(x, y)
            renpy.redraw(self, 0)
```
`event` listens for mouse movement. When the cursor moves within the board boundaries, `hover_coord` is updated using `round_coord` (which snaps the position to the top-left corner of the square under the cursor), and a redraw is requested.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

### ChessDisplayable

`ChessDisplayable` is the core of the chess engine. It handles board rendering, player input, AI moves, game state tracking, and audio.

#### `__init__`

```python
def __init__(self, fen=Start_FEN, player_color=None, depth=10):
    super(ChessDisplayable, self).__init__()
    self.board = chess.Board(fen)
```
A `chess.Board` object is initialized from the given FEN string. This object from python-chess tracks all piece positions, legal moves, check, checkmate, and draw conditions.

```python
    self.whose_turn = chess.WHITE
    self.has_flipped_board = False
    self.history = deque([], Number_History)
```
`whose_turn` tracks which player acts next. `history` is a fixed-length deque that automatically removes the oldest entry when full, keeping only the last 5 moves.

```python
    self.player_color = player_color
    self.bottom_color = self.player_color
    self.uses_stockfish = True
```
`player_color` determines which side the human controls. `bottom_color` controls which color appears at the bottom of the board (and is toggled by the flip button). `uses_stockfish` is `True` when playing against the AI.

```python
    self.engine = global_objects['STOCKFISH_ENGINE']
    self.engine_limit = chess.engine.Limit(depth=depth)
```
The Stockfish engine instance is retrieved from `global_objects` so it persists across screen reloads. The `engine_limit` tells Stockfish how deep to search when calculating its move.

```python
    self.src_coord = None
    self.legal_dsts = []
    self.highlighted_squares = []
```
`src_coord` stores the screen coordinate of the piece the player has clicked. `legal_dsts` is a list of `(file, rank)` index pairs for valid destinations. `highlighted_squares` stores the two squares from the last move for the blue highlight.

```python
    self.show_promotion_ui = False
    self.promotion = None
    self.game_status = None
    self.winner = None
```
Promotion state, overall game status, and the winner are all initialized to `None`.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

#### `render`

```python
def render(self, width, height, st, at):
    render = renpy.Render(width, height)
```
Creates a new render surface for this frame.

```python
    if self.src_coord:
        render.place(self.selected_img,
            x=self.src_coord[0], y=self.src_coord[1],
            width=Loc_Legth, height=Loc_Legth)
```
Draws the turquoise selection highlight on the square the player has clicked.

```python
    for file_idx, rank_idx in self.legal_dsts:
        square_coord = indices_to_coord(file_idx, rank_idx, bottom_color=self.bottom_color)
        render.place(self.legal_dst_img, x=square_coord[0], y=square_coord[1])
```
Draws a pale turquoise dot on every square the selected piece can legally move to.

```python
    for file_idx, rank_idx in self.highlighted_squares:
        square_coord = indices_to_coord(file_idx, rank_idx, bottom_color=self.bottom_color)
        render.place(self.highlight_img, x=square_coord[0], y=square_coord[1])
```
Draws the blue/slate highlight on the two squares (source and destination) of the most recent move.

```python
    for file_idx in range(Index_Min, Index_Max + 1):
        for rank_idx in range(Index_Min, Index_Max + 1):
            piece = self.board.piece_at(chess.square(file_idx, rank_idx))
            if piece and piece.symbol() in self.piece_imgs:
                piece_coord = indices_to_coord(file_idx, rank_idx, bottom_color=self.bottom_color)
                render.place(self.piece_imgs[piece.symbol()],
                    x=piece_coord[0], y=piece_coord[1])
```
Loops over every square on the board. For each square that has a piece, it looks up the piece's image by its symbol (e.g. `'P'` for white pawn, `'p'` for black pawn) and draws it at the correct screen position, accounting for whether the board is flipped.

```python
    renpy.restart_interaction()
    return render
```
`restart_interaction()` forces Ren'Py to re-evaluate screen conditions on the next frame, keeping the status text and other UI in sync with the board state.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

#### `event`

This method handles all player input.

```python
if self.game_status in [Checkmate, Stalemate, Draw]:
    return
```
All input is ignored if the game has ended.

```python
if self.uses_stockfish and self.whose_turn != self.player_color:
    result = self.engine.play(self.board, self.engine_limit)
    self.make_move(result.move)
    return
```
If it is the AI's turn, Stockfish is asked to calculate the best move and `make_move` is called immediately. No player click is needed.

```python
if 0 < x < Board_Size and 0 < y < Board_Size and ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
```
Only left mouse button clicks inside the board area are processed.

**First click — selecting a piece:**
```python
    if self.src_coord is None:
        src_coord = round_coord(x, y)
        src_file, src_rank = coord_to_square(src_coord, bottom_color=self.bottom_color)
        piece = self.board.piece_at(chess.square(src_file, src_rank))
        if piece and piece.color == self.whose_turn:
            self.src_coord = src_coord
            self.get_legal_dsts(src_file, src_rank)
            if self.has_promoting_piece(src_file, src_rank):
                self.show_promotion_ui = True
                self.promotion = None
            renpy.redraw(self, 0)
```
If no piece is currently selected, the clicked square is checked. If it contains a piece belonging to the current player, it is selected. Legal destinations are computed and the promotion UI is shown if the piece is a pawn about to promote.

**Second click — making a move:**
```python
    else:
        dst_coord = round_coord(x, y)
        dst_file, dst_rank = coord_to_square(dst_coord, bottom_color=self.bottom_color)
        src_file, src_rank = coord_to_square(self.src_coord, bottom_color=self.bottom_color)
```
If a piece is already selected, the second click is the destination.

```python
        if dst_file == src_file and dst_rank == src_rank:
            self.src_coord = None
            self.show_promotion_ui = False
            self.legal_dsts = []
            renpy.redraw(self, 0)
            return
```
Clicking the same square again deselects the piece.

```python
        piece = self.board.piece_at(chess.square(dst_file, dst_rank))
        if piece and piece.color == self.whose_turn:
            self.src_coord = dst_coord
            ...
            return
```
Clicking a different piece of the same color switches the selection to that piece instead.

```python
        move = chess.Move(
            chess.square(src_file, src_rank),
            chess.square(dst_file, dst_rank),
            self.promotion
        )
        if self.show_promotion_ui and not move.promotion:
            renpy.notify('Please select a piece type to promote to')
        if move in self.board.legal_moves:
            self.make_move(move)
```
A `chess.Move` object is constructed from the source square, destination square, and the selected promotion piece (if any). If the promotion UI is shown but no piece has been chosen yet, the player is notified. Otherwise if the move is legal it is executed.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

#### Helper Methods

**`load_piece_imgs`**
```python
def load_piece_imgs(self):
    piece_imgs = {}
    for piece in Piece_Types:
        white_path = os.path.join(Chesspieces_File, 'w' + piece + '.png')
        black_path = os.path.join(Chesspieces_File, 'b' + piece + '.png')
        piece_imgs[piece.upper()] = Image(white_path)
        piece_imgs[piece]         = Image(black_path)
    return piece_imgs
```
Builds a dictionary mapping piece symbols to their image objects. For example, `'P'` maps to `wp.png` (white pawn) and `'p'` maps to `bp.png` (black pawn). Images are loaded once at init time.

**`has_promoting_piece`**
```python
def has_promoting_piece(self, file_idx, rank_idx):
    piece = self.board.piece_at(chess.square(file_idx, rank_idx))
    if not piece or not piece.symbol() in ['p', 'P'] or not piece.color == self.whose_turn:
        return False
    if piece.color == chess.WHITE:
        return rank_idx == Promotion_White   # rank 6, one step from rank 7
    else:
        return rank_idx == Promotion_Black   # rank 1, one step from rank 0
```
Checks if the piece on the given square is a pawn belonging to the current player that is one step away from promoting. Returns `True` only if all conditions are met.

**`play_move_audio`**
```python
def play_move_audio(self, move):
    if move.promotion:
        renpy.sound.play(Promotion_Audio)
    else:
        if self.board.is_capture(move):
            renpy.sound.play(Capture_Audio)
        else:
            renpy.sound.play(Move_Audio)
```
Plays the appropriate sound for a move: promotion sound for promotions, capture sound if the move takes a piece, and normal move sound otherwise.

**`check_game_status`**
```python
def check_game_status(self):
    if self.board.is_checkmate():
        self.game_status = Checkmate
        renpy.sound.play(Checkmate_Audio)
        self.winner = not self.whose_turn  # the player whose turn it now is was the one checkmated
        return
    if self.board.is_stalemate():
        self.game_status = Stalemate
        renpy.sound.play(Draw_Audio)
        return
    if self.board.can_claim_threefold_repetition():
        self.game_status == Threefold
        self.show_claim_draw_ui(reason='Threefold repetition rule: ')
    if self.board.can_claim_fifty_moves():
        self.game_status == Fifty_Moves
        self.show_claim_draw_ui(reason='Fifty moves rule: ')
    if self.board.is_check():
        self.game_status = When_Checked
        renpy.sound.play(Check_Audio)
    else:
        self.game_status = None
```
Called after every move. Checks conditions in order of priority — checkmate and stalemate are checked first because they end the game immediately, then draw claims, then check. The winner is set to `not self.whose_turn` because after the move is pushed, `whose_turn` has already been toggled to the next player — so the checkmated player is the current one.

**`show_claim_draw_ui`**
```python
def show_claim_draw_ui(self, reason=''):
    renpy.show_screen('confirm',
        message=reason + 'Would you like to claim draw?',
        yes_action=[Hide('confirm'), Play('sound', Draw_Audio), Return(Draw)],
        no_action=Hide('confirm'))
    renpy.restart_interaction()
```
Shows the built-in Ren'Py confirm screen with an optional reason prefix. If the player accepts, it returns `Draw` to the calling script.

**`add_highlight_move`**
```python
def add_highlight_move(self, move):
    src_file = chess.square_file(move.from_square)
    src_rank = chess.square_rank(move.from_square)
    dst_file = chess.square_file(move.to_square)
    dst_rank = chess.square_rank(move.to_square)
    self.highlighted_squares = [(src_file, src_rank), (dst_file, dst_rank)]
```
Extracts the file and rank indices from both squares of a move and stores them so `render` can draw the blue previous-move highlight.

**`get_legal_dsts`**
```python
def get_legal_dsts(self, src_file, src_rank):
    self.legal_dsts = []
    for move in self.board.legal_moves:
        move_src_file = chess.square_file(move.from_square)
        move_src_rank = chess.square_rank(move.from_square)
        if move_src_file == src_file and move_src_rank == src_rank:
            move_dst_file = chess.square_file(move.to_square)
            move_dst_rank = chess.square_rank(move.to_square)
            self.legal_dsts.append((move_dst_file, move_dst_rank))
```
Iterates over all legal moves in the current position and keeps only those originating from the selected square. The resulting destination indices are stored in `legal_dsts` so they can be drawn as pale turquoise dots.

**`make_move`**
```python
def make_move(self, move):
    self.play_move_audio(move)
    self.board.push(move)
    self.add_highlight_move(move)
    self.history.append(move)
    self.src_coord = None
    self.legal_dsts = []
    renpy.redraw(self, 0)
    self.whose_turn = not self.whose_turn
    self.check_game_status()
    self.show_promotion_ui = False
    self.promotion = None
```
The central method that executes a move. It plays audio, pushes the move to the board, updates highlights and history, clears the selection state, toggles the active player, then checks the resulting game status. Promotion state is always reset at the end.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

## __Helper Functions__

These module-level functions handle coordinate conversion between screen pixels and board indices.

**`coord_to_square`**
```python
def coord_to_square(coord, bottom_color=chess.WHITE):
    x, y = coord
    if bottom_color == chess.WHITE:
        file_idx = x // Loc_Legth
        rank_idx = Index_Max - (y // Loc_Legth)
    else:
        file_idx = Index_Max - x // Loc_Legth
        rank_idx = y // Loc_Legth
    return int(file_idx), int(rank_idx)
```
Converts a screen pixel coordinate to a `(file_index, rank_index)` pair. When white is at the bottom, file increases left-to-right and rank increases bottom-to-top (so rank is inverted from the Y axis). When black is at the bottom, both axes are flipped.

**`indices_to_coord`**
```python
def indices_to_coord(file_idx, rank_idx, bottom_color=chess.WHITE):
    assert Index_Min <= file_idx <= Index_Max and Index_Min <= file_idx <= Index_Max
    if bottom_color == chess.WHITE:
        x = Loc_Legth * file_idx
        y = Loc_Legth * (Index_Max - rank_idx)
    else:
        x = Loc_Legth * (Index_Max - file_idx)
        y = Loc_Legth * rank_idx
    return (x, y)
```
The inverse of `coord_to_square`. Converts board indices to a screen pixel coordinate (top-left corner of that square). Used by `render` to position piece images and highlights. The assertion ensures indices are always within valid board bounds.

**`round_coord`**
```python
def round_coord(x, y):
    x_round = x // Loc_Legth * Loc_Legth
    y_round = y // Loc_Legth * Loc_Legth
    return (x_round, y_round)
```
Snaps a raw pixel coordinate to the top-left corner of the square it falls within. Integer division by `Loc_Legth` finds which square the cursor is in, then multiplying back gives the pixel-aligned corner. Used for both hover highlighting and click detection.

**`square_to_file_rank`**
```python
def square_to_file_rank(square):
    assert len(square) == 2 or len(square) == 3
    square = square[:2]
    file_idx = ord(square[0]) - ord('a')
    rank_idx = int(square[1]) - 1
    return file_idx, rank_idx
```
Converts an algebraic square notation string (e.g. `'e4'` or `'e8q'` for a promotion) to `(file_index, rank_index)`. The file letter is converted by subtracting the ASCII value of `'a'`, giving 0–7. The rank digit is converted by subtracting 1, also giving 0–7. If a third character exists (promotion piece), it is ignored since only the square position is needed.
