#!/usr/local/bin/python3

import os
import random


class PositionAlreadyFullError(Exception):
    def init(self):
        pass


class Player():

    def __init__(self, name='', marker=''):

        self.name = name
        self.marker = marker


board = [' '] * 10


def generate_board():
    """[Generates board for the players to be seen]
    """

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
    """[Assigns opposite markers to each player]

    Args:
        p1 ([Player class object])
        p2 ([Player class object])
    """

    marker = input(f'{p1.name}, Enter your choice (X or O): ').upper()

    while marker not in ['X', 'O']:
        marker = input(
            'Looks like we were given an invalid option, Please try again: ').upper()

    p1.marker = marker
    p2.marker = ({'X', 'O'} - set(marker)).pop()


def check_if_empty(position):
    """ [Takes in position on the board and check if it is already filled or not
    and returns True or False]

    Args:
        position ([int]): [position index in the board list]

    Returns:
        [bool]: [return True if position is empty space else False]
    """

    return board[position] == ' '


def return_empty_positions(board):
    """[Returns a list of empty positions in the board]

    Args:
        board ([List])

    Returns:
        [List]: [contains positions in the [board] list that are empty]
    """
    empty_positions_list = []

    for position in range(1, 10):
        if check_if_empty(position):
            empty_positions_list.append(position)

    return empty_positions_list


def is_board_full():
    """[Checks if the board is full or not]
    """

    for position in range(1, 10):
        if check_if_empty(position):
            return False
    return True


def has_won(marker):
    """[Checking if player with [marker] (either X or O) has won or not]

    Args:
        marker ([str]): [either X or O]

    Returns:
        [bool]: [return True if a player with [marker] has won else False]
    """

    winning_positions_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [
        1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for winning_positions in winning_positions_list:
        if board[winning_positions[0]] == board[winning_positions[1]] == board[winning_positions[2]] == marker:
            return True
    return False


def update_board(position, marker):
    """[Update the board list index at position parameter with marker]

    Args:
        position ([int]): [position index in the board list]
        marker ([str]): [Either X or O]
    """

    board[position] = marker


def player1_turn(player1):
    """[Updates the board with player1's marker]

    Args:
        player1 ([class Player])

    Raises:
        IndexError: [Raised if the entered position is not in range of 1 to 9 (including 9)]
        PositionAlreadyFullError: [Raised if the entered poisition is already filled with a marker(either X or O)]

    Returns:
        [bool]: [returns True if a player1 has won or the board is full else False]
    """

    generate_board()
    if not return_empty_positions(board):
        print("Board might be full")
        return True

    while True:
        try:
            position = int(input(
                f'{player1.name}, Please choose your position(from 1-9): '))
            if position not in range(1, 10):
                raise IndexError
            if not check_if_empty(position):
                raise PositionAlreadyFullError

        except PositionAlreadyFullError:
            print(
                'The position is already full, Please choose another position')
        except ValueError:
            print('Oops!.. you entered an invalid input')
        except IndexError:
            print('Oops!.. you entered an invalid Position')
        except Exception:
            print("Something went wrong")
        else:
            update_board(position, player1.marker)
            break

    if has_won(player1.marker):
        generate_board()
        print(f'Congratulations! {player1.name} has won')
        return True

    if is_board_full():
        generate_board()
        print('The match was a tie')
        return True

    return False


def computer_turn(player2):
    """[updates the board with player2's marker i.e computer]

    Args:
        player2 ([Player class object])

    Returns:
        [bool]: [returns True if a player1 has won or the board is full else False
    """
    
    generate_board()
    empty_pos_list = return_empty_positions(board)
    try:
        player2_move = random.choice(empty_pos_list)
    except IndexError:
        print("Board might be full")
        return True
    update_board(player2_move, player2.marker)

    if has_won(player2.marker):
        generate_board()
        print(f'{player2.name} has won')
        return True

    if is_board_full() or not empty_pos_list:
        generate_board()
        print('The match was a tie')
        return True

    return False


def play():
    """[handles the logic of turns of each player]
    """

    player1 = Player()
    player2 = Player(name='Computer')
    player1.name = input('Player1, Enter you name: ')
    assign_marker(player1, player2)

    # boolean flag which is set to true when player1 makes its turn and set to false when player2 makes its turn
    player1_go = False

    while True:
        if player1_go:
            if computer_turn(player2):
                break
            player1_go = not player1_go

        else:
            if player1_turn(player1):
                break
            player1_go = not player1_go


def replay():
    """[Asks player if they want to play again]

    Returns:
        [bool]
    """
    replay_input = input('Do you want to play again(y or n): ').upper()
    while replay_input not in ['Y', 'N']:
        replay_input = input('Please enter a valid input(y or n): ').upper()

    return replay_input == 'Y'


def main():
    play()
    while replay():
        global board
        board = [' '] * 10
        play()


if __name__ == "__main__":
    os.system('clear')
    main()
