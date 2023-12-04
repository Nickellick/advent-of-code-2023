def main():
    with open('4/input-2.txt', mode='r') as file:
        total_cards_qty = 0
        cards = file.readlines()
        i = 0
        copies = {}
        while i < len(cards):
            cards[i].strip()
            str_contains_id, str_contains_card = cards[i].split(': ')
            id_ = int(str_contains_id.split()[1])
            win_numbers, game_numbers = str_contains_card.split(' | ')
            win_numbers = list(map(int, win_numbers.split()))
            repeats = 1
            if copies.get(i):
                repeats = repeats + copies[i]
            for _ in range(repeats):
                win_number_qty = 0
                total_cards_qty += 1
                for number in map(int, game_numbers.split()):
                    if number in win_numbers:
                        win_number_qty += 1
                for j in range(i + 1, i + 1 + win_number_qty):
                    if j not in copies:
                        copies[j] = 0
                    copies[j] += 1
            i += 1

        print(total_cards_qty)

if __name__ == '__main__':
    main()
