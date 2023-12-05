from get_input import get_advent_of_code_input

seed_map = get_advent_of_code_input(2023, 5, splitlines=False)

def part_one(seed_map):
    def create_mapping(input_str):
        lines = input_str.strip().split("\n")
        return [tuple(map(int, line.split())) for line in lines]

    def map_through_categories(number, mappings):
        for mapping in mappings:
            found = False
            for dest_start, src_start, length in mapping:
                if src_start <= number < src_start + length:
                    number = dest_start + (number - src_start)
                    found = True
                    break
            if not found:
                number = number  
        return number

    sections = seed_map.split("\n\n")

    seeds_section = sections[0]
    seeds = list(map(int, seeds_section.split(":")[1].strip().split()))

    mappings = [create_mapping(section.split(":")[1]) for section in sections[1:]]

    final_locations = [map_through_categories(seed, mappings) for seed in seeds]

    lowest_location = min(final_locations)

    return lowest_location

def part_two(seed_map):
    def create_mapping(input_str):
        mapping = {}
        lines = input_str.strip().split("\n")
        for line in lines:
            dest_start, src_start, length = map(int, line.split())
            for i in range(length):
                mapping[src_start + i] = dest_start + i
        return mapping

    def map_number(number, mapping):
        return mapping.get(number, number) 

    def process_seed_range(start, length, mappings):
        min_location = float('inf')
        for seed in range(start, start + length):
            mapped_number = seed
            for mapping in mappings:
                mapped_number = map_number(mapped_number, mapping)
            min_location = min(min_location, mapped_number)
        return min_location

    sections = seed_map.split("\n\n")

    seeds_section = sections[0]
    seed_ranges = list(map(int, seeds_section.split(":")[1].strip().split()))
    mappings = [create_mapping(section.split(":")[1]) for section in sections[1:]]

    lowest_locations = [process_seed_range(seed_ranges[i], seed_ranges[i + 1], mappings) for i in range(0, len(seed_ranges), 2)]

    overall_lowest_location = min(lowest_locations)

    return overall_lowest_location

print(part_one(seed_map))   
print(part_two(seed_map))