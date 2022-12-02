import sys
import os
import itertools


def parse_input(filename):
    elves_cals = {}
    with open(filename, 'r') as f:
        lines = f.readlines()

        i = 0
        for line in lines:
            if line == '\n':
                i += 1
                continue

            if i in elves_cals:
                elves_cals[i] += int(line)
            else:
                elves_cals[i] = int(line)

    return elves_cals


def get_top_cals(elves_cals, amount):
    sorted_cals = {key: val for key, val in sorted(elves_cals.items(), key = lambda ele: ele[1], reverse=True)}
    max_cals = dict(itertools.islice(sorted_cals.items(), amount))
    print(max_cals)
    return sum(max_cals.values())


if __name__ == '__main__':

    if len(sys.argv) != 2:
        raise ValueError('Please provide a file name with the necessary input values.')

    filename = sys.argv[1]

    if not os.path.isfile(filename):
        raise ValueError('File does not exist.')

    elves_cals = parse_input(filename)
    max_cals = get_top_cals(elves_cals, 3)

    print(max_cals)
