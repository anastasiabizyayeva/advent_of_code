from get_input import get_advent_of_code_input

race_details = get_advent_of_code_input(2023, 6, splitlines=False)

def part_one(race_details):

    lines = race_details.strip().split('\n')

    times = [int(time) for time in lines[0].split()[1:]]
    distances = [int(distance) for distance in lines[1].split()[1:]]

    def calculate_winning_ways(times, records):
        winning_ways = []
        for time, record in zip(times, records):
            ways_to_win = 0
            for hold_time in range(time + 1):
                speed = hold_time
                remaining_time = time - hold_time
                distance = speed * remaining_time
                if distance > record:
                    ways_to_win += 1
            winning_ways.append(ways_to_win)
        return winning_ways

    winning_ways = calculate_winning_ways(times, distances)

    total_ways = 1
    for ways in winning_ways:
        total_ways *= ways

    return total_ways

def part_two(race_details):
    lines = race_details.strip().split('\n')
    time = int(lines[0].split(': ')[1].replace(" ", ""))  
    distance = int(lines[1].split(': ')[1].replace(" ", ""))

    def calculate_winning_ways_single_race(time, record):
        ways_to_win = 0
        for hold_time in range(1, time):
            speed = hold_time
            remaining_time = time - hold_time
            distance_traveled = speed * remaining_time
            if distance_traveled > record:
                ways_to_win += 1
        return ways_to_win

    winning_ways = calculate_winning_ways_single_race(time, distance)

    return winning_ways

print(part_one(race_details))
print(part_two(race_details))