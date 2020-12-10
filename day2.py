import re
from collections import Counter


# PasswordPolicy = namedtuple('PasswordPolicy', ['lower_limit', 'upper_limit', 'character', 'password'])

class PasswordPolicy:
    pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')

    @classmethod
    def parse(cls, password_input):
        match = PasswordPolicy.pattern.match(password_input)
        lower_limit, upper_limit, character, password = match.group(1), match.group(2), match.group(3), match.group(4)
        return PasswordPolicy(int(lower_limit), int(upper_limit), character, password)

    def __init__(self, lower_limit, upper_limit, character, password) -> None:
        self.password = password
        self.character = character
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit

    def is_valid(self) -> bool:
        counter = Counter(self.password)
        count = counter.get(self.character, 0)
        return self.lower_limit <= count <= self.upper_limit

    def is_valid_2(self) -> bool:
        first_index = self.lower_limit - 1
        second_index = self.upper_limit - 1
        return (self.password[first_index] == self.character and self.password[second_index] != self.character) \
               or (self.password[first_index] != self.character and self.password[
            second_index] == self.character)


def solve_part_1(data):
    valid_count = 0
    for pp in data:
        password_policy = PasswordPolicy.parse(pp)
        if password_policy.is_valid():
            valid_count += 1
    return valid_count


def solve_part_2(data):
    valid_count = 0
    for pp in data:
        password_policy = PasswordPolicy.parse(pp)
        if password_policy.is_valid_2():
            valid_count += 1
    return valid_count


if __name__ == '__main__':
    with open('day2_input.txt') as f:
        data = f.read().splitlines()
        result = solve_part_1(data)
        print(result)
        result = solve_part_2(data)
        print(result)


# Other's solution
# -----------------------------------------------------------------------------------
def valid_password_2(line) -> bool:
    "Does line's pw have letter L at position a or b (1-based), but not both?"
    a, b, L, pw = line
    return (L == pw[a-1]) ^ (L == pw[b-1])