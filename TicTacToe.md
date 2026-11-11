# 1. Who are the users?
# 2. What can users do?
# 3. What data exists?
# 4. How does data flow?
# 5. What are the bottlenecks?
# 6. How many users?
# 7. What consistency is required?
# 8. What should happen if something fails?


Design an online multiplayer Tic Tac Toe like chess.com.



Functional Requirement:

1. 2 player cam play
2. one player is X and another is O

3. board 3X3

4. player take turn


5. a move is valid only 
    the player is turn
    the cell is empty
    the games isnt finished

6. detect win or draw

7. restart game


classes:

1. Player
2. Board
3. Cell
4. Move
6. Game
7. Game Status
8. Symbol


1. Player: id, name, symbol
X - check winner, valid baord, manage turn


2. Board: holding cell, updating a cell, checking wether cell is empty, priting the board

X - whose turn, winner, score

3. Game: Current  player, switching turn, calling baord, calling winner check, game lifecycle



5. Move

Player X


Cell (1, 2)

TimeStamp


6. Cell

row 
column
symbol



Relationships


Game - Board, Player X, Player O, Winner Checker


Board - Cell (9)



Move - PLayer


## Design Each Class


## Player:

get_symbol()
get_name()

## Cell:

is_empty()
set_symbol()
clear()

## Board:

3X3 Cells

place_symbol()
is_valid_move()
is_full()

display()

reset()


## Move



## Game

start()
play_move()
switch_turn()

restart()
get_winner()




#####  Who Should Detect Winner?

Board.check_winner()


WinnerChecker - New Class


check()


check_row()

check_column()


check_diagonal()


### string

RUNNING

OVER
DRAW

## Game Status

NOT_STARTED
IN_PROGRESS
DRAW
FINISHED


Symbol

X
O

Empty

