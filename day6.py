from collections import Counter
from functools import reduce
from typing import List

from common import cat


def solve_part_1(data):
    result = []
    for group in data:
        people_answers = group.split('\n')
        counter = get_answer_count(people_answers)
        result.append(len(counter.keys()))
    return sum(result)


def get_answer_count(people_answers):
    counter = Counter()
    for person_answers in people_answers:
        counter = counter + Counter(person_answers)
    return counter


def solve_part_2(data):
    result = []
    for group in data:
        people_answers = group.split('\n')
        number_of_people_in_grp = len(people_answers)
        counter = get_answer_count(people_answers)
        cnt = number_of_answers_answered_by_eachone_in_grp(counter, number_of_people_in_grp)
        result.append(cnt)
    return sum(result)


def number_of_answers_answered_by_eachone_in_grp(counter, number_of_people_in_grp):
    return len([answer for answer, answer_count in counter.items() if answer_count == number_of_people_in_grp])


# another approach would have been to do union & intersection
def solve_part_2_alternate(data):
    result = []
    for group in data:
        people_answers = group.split('\n')
        all_yes_answers = reduce(lambda s1, s2: s1.intersection(s2), [set(answers) for answers in people_answers])
        result.append(len(all_yes_answers))
    return sum(result)


if __name__ == '__main__':
    with open('day6_input.txt') as f:
        data = f.read().split('\n\n')
        result = solve_part_1(data)
        print(result)
        result = solve_part_2(data)
        print(result)

# Other's solution
# ----------------------------------------------------------------------

# assert in6[1] == ['arke', 'qzr', 'plmgnr', 'uriq'] # A group is a list of strs

def day6_1(groups):
    "For each group, compute the number of letters that ANYONE got. Sum them."
    return sum(len(set(cat(group))) for group in groups)


def day6_2(groups: List[List[str]]):
    "For each group, compute the number of letters that EVERYONE got. Sum them."
    return sum(len(set.intersection(*map(set, group)))
               for group in groups)

