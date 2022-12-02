import sys
import os


choice_points = {'A': 1, 'B': 2, 'C': 3}
choice_mappings = {'A': 'X', 'B': 'Y', 'C': 'Z'}
rules = {'A': 'B', 'B': 'C', 'C': 'A'}
inverse_rules = {'B': 'A', 'C': 'B', 'A': 'C'}
mappings = {
    'A': 'Rock',
    'X': 'Rock',
    'B': 'Paper',
    'Y': 'Paper',
    'C': 'Scissors',
    'Z': 'Scissors'
}


def parse_input(filename):
    games = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            choices = tuple([choice.strip() for choice in line.split(' ')])
            games.append(choices)

    return games


def get_choice(opponent_choice, expected_result):
    if expected_result == 'X':
        return inverse_rules[opponent_choice]
    if expected_result == 'Y':
        return opponent_choice
    if expected_result == 'Z':
        return rules[opponent_choice]


def play_game(game):
    points = 0
    opponent_choice = game[0]
    expected_result = game[1]
    player_choice = get_choice(opponent_choice, expected_result)
    points += choice_points[player_choice]

    if rules[opponent_choice] == player_choice:
        points += 6
        print(f'Player wins by choosing {mappings[player_choice]} against {mappings[opponent_choice]}.')
    elif opponent_choice == player_choice:
        points += 3
        print(f'It\'s a draw: {mappings[player_choice]} against {mappings[opponent_choice]}.')
    else:
        print(f'Player loses with {mappings[player_choice]} against {mappings[opponent_choice]}.')

    print(f'Player earns {points} points.')
    return points


if __name__ == '__main__':

    if len(sys.argv) != 2:
        raise ValueError('Please provide a file name with the necessary input values.')

    filename = sys.argv[1]

    if not os.path.isfile(filename):
        raise ValueError('File does not exist.')

    games = parse_input(filename)

    total_points = sum([play_game(game) for game in games])

    print(f'Total points after {len(games)} games: {total_points}')