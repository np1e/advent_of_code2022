import sys
import os


def parse_input(filename):
    assignments = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            assignment = line.split(',')
            first_assignment = assignment[0].split('-')
            first_assignment = list(range(int(first_assignment[0]), int(first_assignment[1]) + 1))
            second_assignment = assignment[1].split('-')
            second_assignment = list(range(int(second_assignment[0]), int(second_assignment[1]) + 1))
            assignments.append((first_assignment, second_assignment))
    return assignments


def check_range_contains(assignment_pair):
    check_one = all(id in assignment_pair[1] for id in assignment_pair[0])
    check_two = all(id in assignment_pair[0] for id in assignment_pair[1])
    if check_one:
        print(f'{assignment_pair[1]} fully contains {assignment_pair[0]}')
    if check_two:
        print(f'{assignment_pair[0]} fully contains {assignment_pair[1]}')
    return check_one or check_two


def check_range_overlaps(assignment_pair):
    overlaps = any(id in assignment_pair[1] for id in assignment_pair[0])
    if overlaps:
        print(f'{assignment_pair[1]} overlaps with {assignment_pair[0]}')
    return overlaps

if __name__ == '__main__':

    if len(sys.argv) != 2:
        raise ValueError('Please provide a file name with the necessary input values.')

    filename = sys.argv[1]

    if not os.path.isfile(filename):
        raise ValueError('File does not exist.')

    assignments = parse_input(filename)

    # part 1: check if one range in any assignment pair contains the other
    range_containments = [check_range_contains(pair) for pair in assignments]
    print(f'In {range_containments.count(True)} assignment pairs one range fully contains the other.')

    # part 2: check if any assignment pairs overlap at all
    range_overlaps = [check_range_overlaps(pair) for pair in assignments]
    print(f'{range_overlaps.count(True)} assignment pairs overlap.')
