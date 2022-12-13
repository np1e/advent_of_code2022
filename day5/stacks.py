import sys
import os
import re

def process_stacks(stacks, num_stacks):
    processed_stacks = [[] for i in range(num_stacks)]
    indices = range(1, num_stacks*4+1, 4)
    for line in stacks:
        i = 0
        for new_stack in processed_stacks:
            if len(line) > indices[i] and not line[indices[i]].isspace():
                new_stack.insert(0, line[indices[i]])
            i += 1

    return processed_stacks


def parse_input(filename):
    stacks = []
    instructions = []
    max_stack_height = 0
    num_stacks = 0
    with open(filename, 'r') as f:
        read_instructions = False
        for line in f.readlines():
            if line.isspace():
                read_instructions = True
                num_stacks = max([int(index) for index in stacks.pop().split()])
                max_stack_height -= 1
                continue

            if read_instructions:
                res, n = re.subn('[a-z]', '', line)
                instructions.append(tuple([int(digit) for digit in res.strip().split()]))
            else:
                stacks.append(line.replace('[', ' ').replace(']', ' ').strip('\n'))
                max_stack_height += 1

    stacks = process_stacks(stacks, num_stacks)
    return stacks, instructions

"""
solution for part 1:
crates are moved one after another (i.e. sequentially)
"""
def move_sequentially(amount, source_stack, target_stack):
    for i in range(amount):
        crate_to_move = source_stack.pop()
        target_stack.append(crate_to_move)


"""
"""
def move_block(amount, source_stack, target_stack):
    crates_to_move = source_stack[len(source_stack)-amount:]
    del source_stack[len(source_stack)-amount:]
    target_stack.extend(crates_to_move)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        raise ValueError('Please provide a file name with the necessary input values.')

    filename = sys.argv[1]

    if not os.path.isfile(filename):
        raise ValueError('File does not exist.')

    stacks, instructions = parse_input(filename)

    for instruction in instructions:
        amount = instruction[0]
        source_stack = stacks[instruction[1]-1]
        target_stack = stacks[instruction[2]-1]
        move_block(amount, source_stack, target_stack)

    top_crates = [stack[-1] for stack in stacks]
    print(f'Crates on top of each stack: {"".join(top_crates)}')