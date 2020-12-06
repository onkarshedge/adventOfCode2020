import re


def height_validation(height):
    m = re.fullmatch(r'(\d+)(cm|in)', height)
    if not m:
        return False
    height_number = int(m.group(1))
    height_unit = m.group(2)
    return (height_unit == 'cm' and 150 <= height_number <= 193) or (height_unit == 'in' and 59 <= height_number <= 76)


mandatory_passport_fields = {
    'byr': lambda birth_year: 1920 <= int(birth_year) <= 2002,
    'iyr': lambda issue_year: 2010 <= int(issue_year) <= 2020,
    'eyr': lambda expiration_year: 2020 <= int(expiration_year) <= 2030,
    'hgt': lambda height: height_validation(height),
    'hcl': lambda hair_color: re.fullmatch(r'#([a-f]|\d){6}', hair_color),
    'ecl': lambda eye_color: re.fullmatch(r'(amb|blu|brn|gry|grn|hzl|oth)', eye_color),
    # 'cid': None,
    'pid': lambda passport_id: re.fullmatch(r'[0-9]{9}', passport_id)
}


def solve_part_1(passports):
    invalid_passports = 0
    for passport in passports:
        for mandatory_field, _ in mandatory_passport_fields.items():
            if mandatory_field not in passport:
                invalid_passports += 1
                break
    return len(passports) - invalid_passports


def parse_passports(data):
    raw_passports: list[list[str]] = [re.split(r'\s+', x) for x in data]
    passports = []
    for raw_passport in raw_passports:
        passport = dict()
        for field in raw_passport:
            field_name, value = field.split(':')
            passport[field_name] = value
        passports.append(passport)
    return passports


def solve_part_2(passports):
    invalid_passports = 0
    for passport in passports:
        for mandatory_field, validation_func in mandatory_passport_fields.items():
            if mandatory_field not in passport or not validation_func(passport[mandatory_field]):
                invalid_passports += 1
                break
    return len(passports) - invalid_passports


if __name__ == '__main__':
    with open('day4_input.txt') as f:
        data = f.read().split('\n\n')
        passports = parse_passports(data)
        result = solve_part_1(passports)
        print(result)
        result = solve_part_2(passports)
        print(result)
