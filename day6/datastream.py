import os
import sys

MARKER_LENGTH = 4
MESSAGE_MARKER_LENGTH = 14

def parse_input(filename):
    with open(filename, 'r') as f:
        return list(f.readline())


def get_marker_pos(datastream, marker_length):
    for i in range(len(datastream)):
        marker = set(datastream[i:i+marker_length])
        if len(marker) == marker_length:
            return i + marker_length


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError('Please provide a file name with the necessary input values.')

    filename = sys.argv[1]

    if not os.path.isfile(filename):
        raise ValueError('File does not exist.')

    datastream = parse_input(filename)
    first_start_marker = get_marker_pos(datastream, MARKER_LENGTH)
    first_message_marker = get_marker_pos(datastream, MESSAGE_MARKER_LENGTH)
    print(f'The first start-of-packet marker is complete after {first_start_marker} characters.')
    print(f'The first start-of-message marker is complete after {first_message_marker} characters.')