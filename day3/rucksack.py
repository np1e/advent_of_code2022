import sys
import os
import string

priorities = {char: priority for (char, priority) in zip(string.ascii_letters, range(1, len(string.ascii_letters)+1))}


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

    if len(sys.argv) != 2:
        raise ValueError('Please provide a file name with the necessary input values.')

    filename = sys.argv[1]

    if not os.path.isfile(filename):
        raise ValueError('File does not exist.')

    rucksacks = parse_input(filename)
    print(rucksacks)
    displaced_items = [item for sublist in (find_displaced_items(rucksack) for rucksack in rucksacks) for item in sublist]
    print(displaced_items)
    total_priorities = sum([priorities[item] for item in displaced_items])

    print(total_priorities)
