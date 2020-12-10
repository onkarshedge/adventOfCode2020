class Instruction:

    def __init__(self, opcode=None, line_number=None, argument=None) -> None:
        self.opcode = opcode
        self.line_number = line_number
        self.argument = argument


def solve_part_1(boot_code):
    program_counter = 0
    accumulator = 0
    visited = set()
    while 0 <= program_counter < len(boot_code):
        instruction = boot_code[program_counter]
        if instruction.line_number in visited:
            return accumulator, False
        if instruction.opcode == 'nop':
            program_counter += 1
        elif instruction.opcode == 'acc':
            program_counter += 1
            accumulator += instruction.argument
        else:  # jmp
            program_counter = program_counter + instruction.argument
        visited.add(instruction.line_number)
    return accumulator, True


def solve_part_2(data):
    for c in range(len(data)):
        boot_code = parse_data(data)
        if boot_code[c].opcode == 'nop':
            boot_code[c].opcode = 'jmp'
        elif boot_code[c].opcode == 'jmp':
            boot_code[c].opcode = 'nop'
        else:
            continue
        acc, terminated = solve_part_1(boot_code)
        if terminated:
            return acc


def parse_data(data):
    program = []
    i = 0
    for line in data:
        opcode, argument = line.split(' ')
        program.append(Instruction(opcode, i, int(argument)))
        i += 1
    return program


if __name__ == '__main__':
    with open('day8_input.txt') as f:
        data = f.read().splitlines()
        boot_code = parse_data(data)
        result = solve_part_1(boot_code)
        print(result)
        result = solve_part_2(data)
        print(result)
