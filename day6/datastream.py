import os
import sys

MARKER_LENGTH = 4

def parse_input(filename):
    with open(filename, 'r') as f:
        return list(f.readline())


def get_marker_pos(datastream):
    marker = set()
    for i in range(len(datastream)):
        marker = set(datastream[i:i+MARKER_LENGTH])
        if len(marker) == MARKER_LENGTH:
            return i + MARKER_LENGTH


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError('Please provide a file name with the necessary input values.')

    filename = sys.argv[1]

    if not os.path.isfile(filename):
        raise ValueError('File does not exist.')

    datastream = parse_input(filename)
    print(get_marker_pos(datastream))