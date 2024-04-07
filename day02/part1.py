AVAILABILITY = {
    'red': 12,
    'green': 13,
    'blue': 14
}


class Game:
    def __init__(self, id, rounds, valid=True):
        self.id = id
        self.rounds = rounds
        self.valid = valid

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


def is_game_valid(game):
    for round in game.rounds:
        for color, availability_count in AVAILABILITY.items():
            if round.get(color, 0) > availability_count:
                return False

    return True


def update_games_validity(games):
    for game in games:
        valid = is_game_valid(game)
        game.valid = valid


def main():
    with open('input.txt') as f:
        games = extract_games(f.readlines())

    update_games_validity(games)

    result = 0
    for game in games:
        if game.valid:
            result += game.id

    print(result)


if __name__ == '__main__':
    main()
