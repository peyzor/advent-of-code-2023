class Game:
    def __init__(self, id, rounds, valid=True):
        self.id = id
        self.rounds = rounds
        self.power = 0

    def __str__(self):
        return f'id: {self.id} rounds: {self.rounds}'


def extract_games(games_info):
    games = []
    for game_info in games_info:
        game_id_info, rounds_info = game_info.split(':')
        game_id = int(game_id_info[5:])

        rounds = []
        for round_info in rounds_info.split(';'):
            round_data = {}
            for ball_info in round_info.split(', '):
                count, name = ball_info.split()
                round_data[name] = int(count)

            rounds.append(round_data)

        game = Game(
            id=game_id,
            rounds=rounds,
        )
        games.append(game)

    return games


def set_games_power(games):
    colors = ['red', 'green', 'blue']
    for game in games:
        min_needed = {}
        for color in colors:
            color_counts = []
            for round in game.rounds:
                color_counts.append(round.get(color, 0))

            min_needed[color] = max(color_counts)

        power = 1
        for color, min_needed_count in min_needed.items():
            power *= min_needed_count

        game.power = power


def main():
    with open('input.txt') as f:
        games = extract_games(f.readlines())

    set_games_power(games)
    print(sum(game.power for game in games))


if __name__ == '__main__':
    main()
