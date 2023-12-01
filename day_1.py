from get_input import get_advent_of_code_input


calibration_lines = get_advent_of_code_input(2023, 1)

def part_one(calibration_lines: list) -> int:
    calibration_value = 0
    for line in calibration_lines:
        digits = [c for c in line if c.isdigit()]
        if digits:
            calibration_value += int(digits[0] + digits[-1])
    return calibration_value

def part_two(calibration_lines: list) -> int:
    spelled_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    calibration_value = 0
    for line in calibration_lines:
        digits = []
        for i, character in enumerate(line):
            if character.isdigit():
                digits.append(character)
            for j, number in enumerate(spelled_nums):
                if line[i:].startswith(number):
                    digits.append(str(j + 1))
        calibration_value += int(digits[0] + digits[-1])
    return calibration_value

print(part_one(calibration_lines))
print(part_two(calibration_lines))