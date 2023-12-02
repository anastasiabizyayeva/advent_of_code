from get_input import get_advent_of_code_input

cube_combos = get_advent_of_code_input(2023, 2)

def part_one(cube_combos: list) -> int:
    goal = {"red": 12, "green": 13, "blue": 14}
    sum_eligible_ids = 0

    for game in cube_combos:
        game_split = game.split(":")
        game_number = int(game_split[0].split(" ")[1])  
        game_results = game_split[1].split(";")

        for round in game_results:
            for cube in round.split(","):
                cube_number, cube_colour = cube.strip().split(" ")
                if goal[cube_colour] < int(cube_number):
                    print(f"Game {game_number} is ineligible because {cube_colour} is too high with {cube_number}")
                    break
            else:
                continue  
            break  
        else:
            print(f"Game {game_number} is eligible with {game_results}")
            sum_eligible_ids += game_number

    return sum_eligible_ids

def part_two(cube_combos: list) -> int:
    sum_power_sets = 0

    for game in cube_combos:
        game_number, game_results = game.split(":")
        game_number = int(game_number.split(" ")[1])
        game_results = game_results.split(";")

        max_values = {"red": 0, "green": 0, "blue": 0}

        for round in game_results:
            for cube in round.split(","):
                cube_number, cube_colour = cube.strip().split(" ")
                cube_number = int(cube_number)

                if cube_number > max_values[cube_colour]:
                    max_values[cube_colour] = cube_number

        if all(value > 0 for value in max_values.values()):
            sum_power_sets += max_values['red'] * max_values['green'] * max_values['blue']

    return sum_power_sets

print(part_one(cube_combos))
print(part_two(cube_combos))