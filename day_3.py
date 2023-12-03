from collections import defaultdict
from get_input import get_advent_of_code_input

engine_schematic = get_advent_of_code_input(2023, 3)

def part_one(schematic: list) -> int:
    def is_symbol(char):
        return not char.isdigit() and char != '.'

    def is_adjacent_to_symbol(x, y):
        directions = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(schematic) and 0 <= ny < len(schematic[0]) and is_symbol(schematic[nx][ny]):
                return True
        return False

    sum_of_parts = 0
    visited = set()
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if (i, j) not in visited and schematic[i][j].isdigit():
                number_str = schematic[i][j]
                k = j + 1
                while k < len(schematic[i]) and schematic[i][k].isdigit():
                    number_str += schematic[i][k]
                    visited.add((i, k))
                    k += 1

                if any(is_adjacent_to_symbol(i, jj) for jj in range(j, k)):
                    sum_of_parts += int(number_str)

    return sum_of_parts

def part_two(schematic: list) -> int:
    rows = len(schematic)
    cols = len(schematic[0])
    gear_to_numbers = defaultdict(list)

    for row in range(rows):
        current_number = 0
        adjacent_gears = set()

        for col in range(len(schematic[row]) + 1):
            if col < cols and schematic[row][col].isdigit():
                current_number = current_number * 10 + int(schematic[row][col])
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= row + dx < rows and 0 <= col + dy < cols:
                            char = schematic[row + dx][col + dy]
                            if not char.isdigit() and char != '.':
                                is_adjacent_to_part = True
                            if char == '*':
                                adjacent_gears.add((row + dx, col + dy))
            elif current_number > 0:
                for gear in adjacent_gears:
                    gear_to_numbers[gear].append(current_number)
                current_number = 0
                adjacent_gears = set()

    sum_of_gear_ratios = 0
    for numbers in gear_to_numbers.values():
        if len(numbers) == 2:
            sum_of_gear_ratios += numbers[0] * numbers[1]

    return sum_of_gear_ratios

print(part_one(engine_schematic))
print(part_two(engine_schematic))