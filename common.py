from bisect import bisect_left


def first(iterable, default=None) -> object:
    "Return first item in iterable, or default."
    return next(iter(iterable), default)


def quantify(iterable, pred=bool) -> int:
    "Count the number of items in iterable for which pred is true."
    return sum(1 for item in iterable if pred(item))


cat = ''.join


def binary_search(sorted_numbers, number_to_search, low_inclusive=0, high_exclusive=None):
    if not high_exclusive:
        high_exclusive = len(sorted_numbers)
    index = bisect_left(sorted_numbers, number_to_search, low_inclusive, high_exclusive)
    if high_exclusive > index >= low_inclusive and sorted_numbers[index] == number_to_search:
        return index
    return -1
