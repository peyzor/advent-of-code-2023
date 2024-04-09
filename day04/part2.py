from collections import defaultdict


class Card:
    def __init__(self, id, win_nums, lose_nums):
        self.id = id
        self.win_nums = win_nums
        self.lose_nums = lose_nums

    def __repr__(self):
        return f'#{self.id}'


CARDS = []
CARDS_COUNT = defaultdict(int)


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


def main():
    original_cards = []
    with open('input.txt') as f:
        for line in f:
            card = create_card(line)
            CARDS.append(card)
            CARDS_COUNT[card.id] += 1
            original_cards.append(card)

    for i in range(len(CARDS)):
        card = CARDS[i]
        matched_nums = set(card.win_nums) & set(card.lose_nums)
        times = CARDS_COUNT[card.id]

        c = 1 if len(matched_nums) > 0 else 0
        while matched_nums and c <= len(matched_nums) and i + c < len(original_cards):
            for _ in range(times):
                won_card = original_cards[i + c]
                CARDS.append(won_card)
                CARDS_COUNT[won_card.id] += 1

            c += 1

    print(len(CARDS))


if __name__ == '__main__':
    main()
