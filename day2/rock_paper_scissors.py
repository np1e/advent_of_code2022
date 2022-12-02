import sys
import os


choice_points = {'X': 1, 'Y': 2, 'Z': 3}
choice_mappings = {'A': 'X', 'B': 'Y', 'C': 'Z'}
rules = {'A': 'Y', 'B': 'Z', 'C': 'X'}
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


def play_game(game):
    points = 0
    opponent_choice = game[0]
    player_choice = game[1]
    points += choice_points[player_choice]

    if rules[opponent_choice] == player_choice:
        points += 6
        print(f'Player wins by choosing {mappings[player_choice]} against {mappings[opponent_choice]}.')
    elif choice_mappings[opponent_choice] == player_choice:
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