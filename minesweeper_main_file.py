from minesweeper_class import Board
import re

def play(dim_size=10, num_bombs=10):
    board = Board(dim_size, num_bombs)
    safe = True 

    while len(board._dug) < board._dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board._dim_size or col < 0 or col >= board._dim_size:
            print("Invalid location. Try again.")
            continue
        safe = board.dig(row, col)
        if not safe:
            break
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
    else:
        print("SORRY GAME OVER :(")
        board._dug = [(r,c) for r in range(board._dim_size) for c in range(board._dim_size)]
        print(board)

if __name__ == '__main__': 
    play()