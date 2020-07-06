import os
from random import randint


class Player():

    def __init__(self, name='', marker=''):

        self.name = name
        self.marker = marker


board_list = [' '] * 10


def generate_board():
    os.system('clear')
    print('     |     |     ')
    print(f'  {board_list[1]}  |  {board_list[2]}  |  {board_list[3]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {board_list[4]}  |  {board_list[5]}  |  {board_list[6]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {board_list[7]}  |  {board_list[8]}  |  {board_list[9]}  ')
    print('     |     |     ')


def assign_marker(p1, p2):
    marker = input(f'{p1.name}, Enter your choice (X or O): ').upper()

    while marker not in ['X', 'O']:
        marker = input(
            'Looks like we were given an invalid option, Please try again: ').upper()

    p1.marker = marker
    p2.marker = ({'X', 'O'} - set(marker)).pop()


def check_if_empty(position):

    return board_list[position] == ' '


def is_board_full():

    empty_pos_list = []

    for i in range(1, 10):
        if check_if_empty(i):
            empty_pos_list.append(i)
            return (False, empty_pos_list)

    return (True, empty_pos_list)


def has_won(marker):
    """[Checking if player with marker (either X or O) has won or not]

    Args:
        marker ([str]): [either X or O]

    Returns:
        [bool]
    """

    return (
        # first row
        board_list[1] == board_list[2] == board_list[3] == marker or
        # second row
        board_list[4] == board_list[5] == board_list[6] == marker or
        # third row
        board_list[7] == board_list[8] == board_list[9] == marker or
        # first column
        board_list[1] == board_list[4] == board_list[7] == marker or
        # second column
        board_list[2] == board_list[5] == board_list[8] == marker or
        # third column
        board_list[3] == board_list[6] == board_list[9] == marker or
        # first diagonal
        board_list[1] == board_list[5] == board_list[9] == marker or
        # second diagonal
        board_list[3] == board_list[5] == board_list[7] == marker
    )


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


