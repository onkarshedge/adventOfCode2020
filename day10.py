# from functools import lru_cache


def solve_part_1(numbers: list[int]) -> int:
    sorted_adapters = sorted(numbers)
    cnt_of_1_difference = 0
    cnt_of_3_difference = 0
    for i in range(len(sorted_adapters) - 1):
        diff = sorted_adapters[i + 1] - sorted_adapters[i]
        if diff == 1:
            cnt_of_1_difference += 1
        elif diff == 3:
            cnt_of_3_difference += 1
    return cnt_of_1_difference * cnt_of_3_difference


def solve_part_2_dp(numbers: list[int]) -> int:
    numbers = set(numbers)
    dp = [0] * 200
    dp[0] = 1
    dp[1] = 1 if 1 in numbers else 0
    dp[2] = 1 + dp[1] if 2 in numbers else 0
    max_joltage = max(numbers)
    for i in range(3, max_joltage + 1):
        if i in numbers:  # O(1) lookup
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        else:
            dp[i] = 0
    return dp[max_joltage]


# alternate forward dp memoized
def solve_part2_dp(numbers: list[int]) -> int:
    joltages = sorted(numbers[:])

    DP = {}

    # @lru_cache
    def dp(index):
        if index == len(joltages) - 1:
            return 1
        if index in DP:
            return DP[index]
        total = 0
        next_index = index + 1
        while next_index < len(joltages) and joltages[next_index] - joltages[index] <= 3:
            total += dp(next_index)
            next_index += 1

        DP[index] = total
        return total

    return dp(0)


def parse_data(data: list[str]) -> list[int]:
    return [int(line) for line in data]


if __name__ == '__main__':
    with open('day10_input.txt') as f:
        data = f.read().splitlines()
        numbers = parse_data(data)
        numbers.append(0)
        numbers.append(max(numbers) + 3)
        result = solve_part_1(numbers)
        print(result)
        result_2 = solve_part_2_dp(numbers)
        print(result_2)
        # result_2 = solve_part2_dp(numbers)
        # print(result_2)

# 347250213298688
