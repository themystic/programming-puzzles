#!/usr/bin/env python
"""
My first Conway's Game of Life. Rather naive (no fancy tricks) and bordered
(all cells outside of the border of the seed are considered dead).
"""

import argparse

ALIVE = '*'
DEAD = '.'


def compute_next_generation(current_generation: [[str]], rows: int,
                            columns: int) -> [[str]]:
    next_generation = list()
    for r in range(rows):
        row = list()
        next_generation.append(row)
        for c in range(columns):
            neighbours = count_neighbours(current_generation, r, c, rows,
                                          columns)
            if (current_generation[r][c] == ALIVE and
                    has_enough_neighbours(neighbours)):
                new_cell_value = ALIVE
            elif (current_generation[r][c] == DEAD and
                    is_resurrectable(neighbours)):
                new_cell_value = ALIVE
            else:
                new_cell_value = DEAD
            row.append(new_cell_value)
    return next_generation


def count_neighbours(board: [[str]], row: int, column: int, rows, columns) -> int:
    neighbours = 0
    for r in range(row - 1, row + 2):
        for c in range(column - 1, column + 2):
            if (0 <= r < rows and  # legal row
                    0 <= c < columns and  # legal column
                    not (r == row and c == column)):  # ignore the cell itself
                if board[r][c] == ALIVE:
                    neighbours += 1
    return neighbours


def is_resurrectable(neighbours: int) -> bool:
    return neighbours == 3


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="A version of Conway's Game of Life")
    parser.add_argument('generations', type=int, default=1)
    parser.add_argument('start', type=argparse.FileType('r'))
    return parser


def main():
    parser = make_parser()
    arguments = parser.parse_args()
    generations = arguments.generations
    board = parse_file(arguments.start)
    print_board(board)
    rows = len(board)
    columns = len(board[0])
    for n in range(generations):
        print_hr()
        board = compute_next_generation(board, rows, columns)
        print_board(board)


def print_hr():
    print(15 * '=')


def has_enough_neighbours(neighbours):
    return 2 <= neighbours <= 3


def parse_file(start_file) -> list:
    with start_file as start_file:
        board = [list(line[:-1]) for line in start_file if line[0] in (DEAD, ALIVE,)]
        max_columns = len(max(board, key=lambda row: len(row)))
        for index, row in enumerate(board):
            columns = len(row)
            board[index] = row + list(DEAD * (max_columns - columns))
        return board


def print_board(board: list):
    for row in board:
        print(''.join(row))


if __name__ == '__main__':
    main()
