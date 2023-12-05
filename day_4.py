from get_input import get_advent_of_code_input

scratch_cards = get_advent_of_code_input(2023, 4)

def part_one(scratch_cards: list) -> int:

    overall_points = 0

    for scratch_card in scratch_cards:
        scratch_card_points = 0
        card_number, comparison_numbers = scratch_card.split(":")
        card_numbers, winning_numbers = comparison_numbers.split("|")
        card_number_list = [int(x.strip()) for x in card_numbers.split(" ") if x.strip()]
        winning_number_list = [int(x.strip()) for x in winning_numbers.split(" ") if x.strip()]

        for number in card_number_list:
            if number in winning_number_list:
                if scratch_card_points == 0:
                    scratch_card_points = 1
                else:
                    scratch_card_points = scratch_card_points * 2
        
        overall_points += scratch_card_points
        
    return overall_points

def part_two(scratch_cards: list) -> int:
    def get_matching_numbers(card_numbers, winning_numbers):
        return len(set(card_numbers) & set(winning_numbers))

    card_matches = []
    for scratch_card in scratch_cards:
        _, comparison_numbers = scratch_card.split(":")
        card_numbers, winning_numbers = comparison_numbers.split("|")
        card_number_list = [int(x.strip()) for x in card_numbers.split(" ") if x.strip()]
        winning_number_list = set(int(x.strip()) for x in winning_numbers.split(" ") if x.strip())
        matches = get_matching_numbers(card_number_list, winning_number_list)
        card_matches.append(matches)

    card_counts = [1] * len(scratch_cards)  

    for i in range(len(card_matches)):
        matches = card_matches[i]
        for j in range(1, matches + 1):
            if i + j < len(card_counts):
                card_counts[i + j] += card_counts[i]

    total_cards = sum(card_counts)
    return total_cards


print(part_one(scratch_cards))
print(part_two(scratch_cards))