# -*- coding: utf-8 -*-

# python imports
import sys
import json


def calculate_super_food (board):

    num_of_super_food = 0
    super_food = u"s"
    for cell in board:
        if super_food in cell:
            num_of_super_food += 1

    return num_of_super_food


def is_map_correct(map_config):
    ghosts = map_config['players']['ghosts']
    board = map_config['board']
    ghost_positions = []
    is_correct = True
    board_width = len(board[0])
    board_height = len(board)
    total_seeds = board_width * board_height
    num_of_super_food = calculate_super_food(board)

    # check ghost positions
    for ghost in ghosts:
        ghost_positions.append(ghost['position'])

    for ghost_pos in ghost_positions:
        if board[ghost_pos[1]][ghost_pos[0]] == 'w':
            print('Invalid ghost position')
            is_correct = False
            break
    # check number_of_super_food
    if num_of_super_food/total_seeds > .025:
        print("Number of super foods are out of range!!!")
        is_correct = False

    # check number of ghosts:
    return is_correct
    

def load_file(map_path):
    with open((map_path), "r") as map_file:
        map_config = json.loads(map_file.read())

    return map_config


if __name__ == '__main__':

    map_path = sys.argv[1]
    map_config = load_file(map_path)
    if is_map_correct(map_config):
        print("Well Done")
    else:
        exit()
