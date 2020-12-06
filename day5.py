import operator
from functools import reduce


def get_column_number(column_info):
    high = 7
    low = 0
    for c in column_info:
        mid = low + ((high - low) >> 1)
        if c == "L":
            high = mid
        else:
            low = mid + 1
    return low


def get_row_number(row_info):
    high = 127
    low = 0
    for c in row_info:
        mid = low + ((high - low) >> 1)
        if c == "F":
            high = mid
        else:
            low = mid + 1
    return low


def solve_part_1(data):
    seat_ids = [get_seat_id(seat_information) for seat_information in data]
    return max(seat_ids)


def get_seat_id(seat_information):
    row_number = get_row_number(seat_information[:7])
    column_number = get_column_number(seat_information[7:])
    return row_number * 8 + column_number


def find_missing_number(numbers, start_inclusive, end_inclusive):
    xor_range = 0
    for i in range(start_inclusive, end_inclusive + 1):
        xor_range = xor_range ^ i
    xor_of_numbers = reduce(operator.xor, numbers)  # lambda x, y: x ^ y operator is faster than lambda '^'
    return xor_of_numbers ^ xor_range


def solve_part_2(data):
    seat_ids = [get_seat_id(seat_information) for seat_information in data]
    minimum = min(seat_ids)
    maximum = max(seat_ids)
    return find_missing_number(seat_ids, minimum, maximum)
    # for index, seat in enumerate(sorted(seat_ids)):
    #     if seat - minimum != index:
    #         return seat - 1


if __name__ == '__main__':
    with open('day5_input.txt') as f:
        data = f.read().splitlines()
        result = solve_part_1(data)
        print(result)
        result = solve_part_2(data)
        print(result)
