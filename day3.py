# from functools import reduce
import math

TREE = '#'


def solve_part_1(map, dx, dy):
    height = len(map)
    width = len(map[0])
    x, y = 0, 0
    count_trees = 0
    while y < (height - dy):
        x = (x + dx) % width
        y = y + dy
        if map[y][x] == TREE:
            count_trees += 1
    return count_trees


def solve_part_2(map):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_at_each_slope = [solve_part_1(map, slope[0], slope[1]) for slope in slopes]
    return math.prod(trees_at_each_slope)


if __name__ == '__main__':
    with open('day3_input.txt') as f:
        data = f.read().splitlines()
        result = solve_part_1(data, 3, 1)
        print(result)
        result = solve_part_2(data)
        print(result)
