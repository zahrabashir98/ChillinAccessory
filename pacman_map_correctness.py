# -*- coding: utf-8 -*-
# python imports
import sys
import json


def is_map_correct(my_map):
    ghosts = my_map['players']['ghosts']
    board = my_map['board']
    ghost_positions = []
    is_correct = True
    for ghost in ghosts:
        ghost_positions.append(ghost['position'])

    for ghost_pos in ghost_positions:
        if board[ghost_pos[1]][ghost_pos[0]] == 'w':
            print('Invalid ghost position')
            is_correct = False
            break
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
