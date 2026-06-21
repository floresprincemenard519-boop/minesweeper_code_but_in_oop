import random 

class Board:
    def __init__(self, dim_size, num_bombs):
        self._dim_size = dim_size
        self._num_bombs = num_bombs
        self._board = self.make_new_board()
        self._assign_values_to_board()
        self._dug = set()

    def make_new_board(self):
        board = [[None for _ in range(self._dim_size)] for _ in range(self._dim_size)]
        bombs_planted = 0
        while bombs_planted < self._num_bombs:
            loc = random.randint(0, self._dim_size**2 - 1) 
            row = loc // self._dim_size  
            col = loc % self._dim_size 
            if board[row][col] == '*':
                continue
            board[row][col] = '*'
            bombs_planted += 1
        return board
    def _assign_values_to_board(self):
        for r in range(self._dim_size):
            for c in range(self._dim_size):
                if self._board[r][c] == '*':
                    continue
                self._board[r][c] = self.get_num_neighboring_bombs(r, c)
    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self._dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self._dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self._board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs
    def dig(self, row, col):
        self._dug.add((row, col))
        if self._board[row][col] == '*':
            return False
        elif self._board[row][col] > 0:
            return True
        for r in range(max(0, row-1), min(self._dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self._dim_size-1, col+1)+1):
                if (r, c) in self._dug:
                    continue
                self.dig(r, c)
        return True
    def __str__(self):
        visible_board = [[None for _ in range(self._dim_size)] for _ in range(self._dim_size)]
        for row in range(self._dim_size):
            for col in range(self._dim_size):
                if (row,col) in self._dug:
                    visible_board[row][col] = str(self._board[row][col])
                else:
                    visible_board[row][col] = ' '
        string_rep = ''
        widths = []
        for idx in range(self._dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )
        indices = [i for i in range(self._dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self._dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len
    
        return string_rep
    
