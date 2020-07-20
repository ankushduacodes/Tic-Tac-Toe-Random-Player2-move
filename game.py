import os
import random


class PositionAlreadyFullError(Exception):
    def init(self):
        pass


class Player():

    def __init__(self, name='', marker=''):

        self.name = name
        self.marker = marker


board = ['X'] * 10


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


def return_empty_positions(board):

    empty_positions_list = []

    for position in range(1, 10):
        if check_if_empty(position):
            empty_positions_list.append(position)

    return empty_positions_list


def is_board_full():

    for position in range(1, 10):
        if check_if_empty(position):
            return False
    return True


def has_won(marker):

    winning_positions_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [
        1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for winning_positions in winning_positions_list:
        if board[winning_positions[0]] == board[winning_positions[1]] == board[winning_positions[2]] == marker:
            return True
    return False


def update_board(position, marker):

    board[position] = marker


def player1_turn(player1):

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

    else:
        return False


def computer_turn(player2):
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

    else:
        return False


def play():

    player1 = Player()
    player2 = Player(name='Computer')
    player1.name = input('Player1, Enter you name: ')
    assign_marker(player1, player2)

    player1_go = False

    while True:
        if player1_go:
            if computer_turn(player2):
                break
            player1_go = not player1_go

        else:
            if player1_turn(player1)
            break
            player1_go = not player1_go


def replay():

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
