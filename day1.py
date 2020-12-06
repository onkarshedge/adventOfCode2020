def two_numbers_with_sum(numbers: list, required_sum: int) -> tuple:
    sorted_numbers = sorted(numbers)
    i = 0
    j = len(numbers) - 1
    while i <= j:
        first_number, second_number = sorted_numbers[i], sorted_numbers[j]
        current_sum = first_number + second_number
        if current_sum > required_sum:
            j -= 1
        elif current_sum < required_sum:
            i += 1
        else:
            return (first_number, second_number)
    return None


def solve_part_1(numbers):
    two_numbers = two_numbers_with_sum(numbers, 2020)
    if two_numbers:
        print(two_numbers)
        x, y = two_numbers
        return x * y


def solve_part_2(numbers):
    for num in numbers:
        required_sum_for_two_numbers = 2020 - num
        numbers_with_sum = two_numbers_with_sum(numbers, required_sum_for_two_numbers)
        if numbers_with_sum:
            x, y = numbers_with_sum
            print(num, x, y)
            return num * x * y


if __name__ == '__main__':
    with open('day1_input.txt') as f:
        data = f.read().splitlines()
        numbers = [int(x) for x in data]
        result = solve_part_1(numbers)
        print(result)
        result = solve_part_2(numbers)
        print(result)
