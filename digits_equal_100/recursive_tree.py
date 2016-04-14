import operator

from functools import reduce

DIGITS = '123456789'


def get_numbers_from_digits_left(digits_left):
    return ((int(digits_left[:n]), digits_left[n:]) for n in range(1, len(digits_left) + 1))


def print_solution(operations):
    prefixed_solution = " ".join((" ".join(("+" if op == operator.add else "-", str(number)))
                                  for op, number in operations))
    print(prefixed_solution[1:])


def calculate_solution(operations, digits_left):
    if not digits_left:
        total = reduce(lambda total, optor_num_pair: optor_num_pair[0](total, optor_num_pair[1]),
                       operations,
                       0)
        if total == 100:
            print_solution(operations)
        return
    else:
        for number, new_digits_left in get_numbers_from_digits_left(digits_left):
            calculate_solution(operations + [(operator.add, number)], new_digits_left)
            if digits_left != DIGITS:
                calculate_solution(operations + [(operator.sub, number)], new_digits_left)


calculate_solution(list(), DIGITS)
