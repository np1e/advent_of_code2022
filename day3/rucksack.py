import sys
import os
import string

priorities = {char: priority for (char, priority) in zip(string.ascii_letters, range(1, len(string.ascii_letters)+1))}


def get_badge_for_group(group):
    flattened_rucksacks = [rucksack[0] + rucksack[1] for rucksack in group]
    return [item for item in flattened_rucksacks[0] if item in flattened_rucksacks[1] and item in flattened_rucksacks[2]]


def find_displaced_items(rucksack):
    return set([item for item in rucksack[0] if item in rucksack[1]])


def parse_input(filename):
    rucksacks = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            rucksack = line.strip()
            compartments = (rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:])
            rucksacks.append(compartments)

    return rucksacks


if __name__ == '__main__':

    if len(sys.argv) < 2:
        raise ValueError('Please provide a file name with the necessary input values.')

    filename = sys.argv[1]
    group_size = int(sys.argv[2]) if len(sys.argv) == 3 else 3

    if not os.path.isfile(filename):
        raise ValueError('File does not exist.')

    rucksacks = parse_input(filename)
    displaced_items = [item for sublist in (find_displaced_items(rucksack) for rucksack in rucksacks) for item in sublist]
    total_priorities = sum([priorities[item] for item in displaced_items])

    print(f'Sum of priorities for all items that appear in both compartments of a rucksack: {total_priorities}')

    badges = [get_badge_for_group(group)[0] for group in [[rucksacks[i], rucksacks[i+1], rucksacks[i+2]] for i in range(0, len(rucksacks), group_size)]]
    print(f'Bagdes for each group:')
    for i in range(len(badges)):
        print(f'\t{i+1}. group: {badges[i]}')

    badge_priorities = sum([priorities[badge] for badge in badges])
    print(f'Sum of priorities for all badges: {badge_priorities}')
