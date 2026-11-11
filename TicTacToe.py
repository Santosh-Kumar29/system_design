from enum import Enum
from abc import ABC, abstractmethod

class PlayerSymbol(Enum):
    X = "X"
    O = "O"
    EMPTY = "EMPTY"
    
    
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    
class GameState(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def handle(self, game, row, col):
        pass
    
    @abstractmethod
    def is_game_over(self):
        pass
    

class RunningState(GameState):
    def handle(self, game, row, col):
        if not self.is_valid_move(game, row, col):
            print("Invalid move")
            return self
        game.board[row][col] = game.current_player.get_symbol()
        
        if game.has_winner(game.current_player.get_symbol()):
            print(f"{game.current_player.get_symbol()} Wins")
            if game.current_player.get_symbol() == PlayerSymbol.X:
                return XWinsState()
            else:
                return OWinsState()
        elif game.is_draw():
            print("Draw")
            return DrawState()
        
        return RunningState()
    
    def is_game_over(self):
        return False
    
    def is_valid_move(self, game, row, col, board_size=3):
        if row < 0 or row >= board_size or col < 0 or col >= board_size:
            return False
        if game.board[row][col] != PlayerSymbol.EMPTY:
            return False
        return True
    
class XWinsState(GameState):
    def handle(self, game, row, col):
        print("X Wins")
        return XWinsState()
    
    def is_game_over(self):
        return True
    
class OWinsState(GameState):
    def handle(self, game, row, col):
        print("O Wins")
        return OWinsState()
    
    def is_game_over(self):
        return True
    
class DrawState(GameState):
    def handle(self, game, row, col):
        print("Draw")
        return DrawState()
    
    def is_game_over(self):
        return True
    
class Game:
    def __init__(self):
        self.state = RunningState()
        ## 3X3 matrix
        self.board = [[PlayerSymbol.EMPTY for _ in range(3)] for _ in range(3)]
        self.player_x = Player("Player X", PlayerSymbol.X)
        self.player_o = Player("Player O", PlayerSymbol.O)
        self.current_player = self.player_x
    
    def get_move(self):
        return int(input("Enter the row: ")), int(input("Enter the column: "))
    
    def start_game(self):
        while not self.state.is_game_over():
            row, col = self.get_move()
            self.state = self.state.handle(self, row, col)
            self.switch_turn()
            
    def is_draw(self):
        for row in self.board:
            for cell in row:
                if cell == PlayerSymbol.EMPTY:
                    return False
        return True
    def switch_turn(self):
        if self.current_player == self.player_x:
            self.current_player = self.player_o
        else:
            self.current_player = self.player_x
    
    def has_winner(self, symbol):
        
        ## horizontal check
        for row in self.cells:
            if row[0] == row[1] == row[2] == symbol:
                return True

        for col in range(3):
            if (
                self.cells[0][col]
                == self.cells[1][col]
                == self.cells[2][col]
                == symbol
            ):
                return True

        left_diagonal = (
            self.cells[0][0] == self.cells[1][1] == self.cells[2][2] == symbol
        )
        right_diagonal = (
            self.cells[0][2] == self.cells[1][1] == self.cells[2][0] == symbol
        )

        return left_diagonal or right_diagonal
    
    

# Game
# │
# ├── Board
# │      ├── Cell[][]
# │      └── BoardSize
# │
# ├── Players
# │
# ├── GameStatus
# │
# ├── Move
# │
# ├── WinnerStrategy
# │
# ├── DiagonalStrategy
# │
# ├── RowStrategy
# │
# └── ColumnStrategy