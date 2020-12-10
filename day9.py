from bisect import bisect_left
from collections import deque
from itertools import combinations

from common import first, binary_search


def solve_part_1(numbers, preamble) -> tuple[int, int]:
    for i in range(preamble, len(numbers)):
        found = False
        for k in range(preamble - 1):
            for l in range(k + 1, preamble):
                if numbers[i - preamble + k] + numbers[i - preamble + l] == numbers[i]:
                    found = True
                    break
            if found:
                break
        if not found:
            return i, numbers[i]

# O(nlogn) solution
def solve_part_2(numbers, required_sum, required_sum_index):
    continuous_sub_array_indices = find_continuous_sub_array_with_sum(numbers, required_sum, required_sum_index)
    if continuous_sub_array_indices:
        start, end = continuous_sub_array_indices
        print(continuous_sub_array_indices)
        return min(numbers[start:end + 1]) + max(numbers[start:end + 1])


def get_prefix_sum(numbers: list[int]) -> list[int]:
    """
    :param numbers:
    :return: list with size + 1 and first element as 0
    """
    if not numbers:
        return []
    length = len(numbers)
    prefix_sum = [0] * (length + 1)
    prefix_sum[1] = numbers[0]
    for i in range(2, length + 1):
        prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]
    return prefix_sum




def find_continuous_sub_array_with_sum(numbers: list[int], required_sum: int, required_sum_index=None) -> tuple[
    int, int]:
    """
    :param numbers: list of integers
    :param required_sum: sum of a continuous sub array should be equal to this
    :param required_sum_index: optional If the sum is already a number present in the list.
    :return:
        a start index and end index both inclusive of the sub array. the sub array of at least size 2.
    """
    if not required_sum_index:
        required_sum_index = len(numbers)
    prefix_sum = get_prefix_sum(numbers)
    for idx, first_of_pair in enumerate(prefix_sum[:-1]):
        other = required_sum + first_of_pair
        search_item_index = binary_search(prefix_sum, other, idx + 1, required_sum_index + 1)
        if search_item_index != -1:
            return idx, search_item_index - 1


def parse_data(data):
    return [int(line) for line in data]


if __name__ == '__main__':
    with open('day9_input.txt') as f:
        data = f.read().splitlines()
        numbers = parse_data(data)
        result = solve_part_1(numbers, 25)
        print(result)
        result_2 = solve_part_2(numbers, result[1], result[0])
        print(result_2)


# ----------------------------------------------------------------------------------------------------
# other's solution for part_1

def day9_1(nums, p=25):
    """Find the first number in the list of numbers (after a preamble of p numbers)
    which is not the sum of two of the p numbers before it."""
    return first(x for i, x in enumerate(nums) if i > p and x not in sum2(nums[i - p:i]))


def sum2(nums): return map(sum, combinations(nums, 2))


# other's solution for part 2
def day9_2(nums, target):
    "Find a contiguous subsequence of nums that sums to target; add their max and min."
    subseq = find_subseq(nums, target)
    return max(subseq) + min(subseq)


def find_subseq(nums, target) -> deque:
    "Find a contiguous subsequence of nums that sums to target."
    subseq = deque()
    total = 0
    for x in nums:
        if total < target:
            subseq.append(x)
            total += x
        if total == target:
            return subseq
        while total > target:
            total -= subseq.popleft()

