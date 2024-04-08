class Card:
    def __init__(self, id, win_nums, lose_nums):
        self.id = id
        self.win_nums = win_nums
        self.lose_nums = lose_nums
        self.points = 0

    def __str__(self):
        return f'id: {self.id}'


def create_card(line):
    card_id_part, numbers_part = line.split(':')
    card_id = int(card_id_part[5:])

    win_nums_part, lose_nums_part = numbers_part.split('|')
    lose_nums = [int(n) for n in lose_nums_part.split()]
    win_nums = [int(n) for n in win_nums_part.split()]
    card = Card(
        id=card_id,
        lose_nums=lose_nums,
        win_nums=win_nums
    )
    return card


def calculate_card_points(card):
    matched_win_nums = set(card.win_nums) & set(card.lose_nums)
    if not matched_win_nums:
        return 0

    return 2 ** (len(set(card.win_nums) & set(card.lose_nums)) - 1)


def main():
    cards = []
    with open('input.txt') as f:
        for line in f:
            card = create_card(line)
            card.points = calculate_card_points(card)
            cards.append(card)

    print(sum(card.points for card in cards))


if __name__ == '__main__':
    main()
