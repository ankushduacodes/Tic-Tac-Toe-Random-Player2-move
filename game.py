import os
from random import randint


class Player():

    def __init__(self, name='', marker=''):

        self.name = name
        self.marker = marker


board = [' '] * 10


def generate_board():
    os.system('clear')
    print('     |     |     ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print('     |     |     ')


def assign_marker(p1, p2):
    marker = input(f'{p1.name}, Enter your choice (X or O): ').upper()

    while marker not in ['X', 'O']:
        marker = input(
            'Looks like we were given an invalid option, Please try again: ').upper()

    p1.marker = marker
    p2.marker = ({'X', 'O'} - set(marker)).pop()


def check_if_empty(position):

    return board[position] == ' '


def is_board_full():
    
    """[summary]

    Returns:
        [type]: [description]
    """

    empty_pos_list = []

    for i in range(1, 10):
        if check_if_empty(i):
            empty_pos_list.append(i)

    if empty_pos_list:
        return (False, empty_pos_list)
    else:
        return (True, empty_pos_list)


def has_won(marker):
    """[Checking if player with marker (either X or O) has won or not]

    Args:
        marker ([str]): [either X or O]

    Returns:
        [bool]
    """

    winning_positions_list = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    
    for winning_positions in winning_positions_list:
        if board[winning_positions[0]] == board[winning_positions[1]] == board[winning_positions[2]] == marker:
            return True
    return False



def play():
    player1 = Player()
    player2 = Player(name='Computer')
    player1.name = input('Player1, Enter you name: ')
    assign_marker(player1, player2)
    generate_board()


def main():
    play()


if __name__ == "__main__":
    os.system('clear')
    main()
