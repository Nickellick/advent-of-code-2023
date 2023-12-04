def main():
    with open('4/input-1.txt', mode='r') as file:
        points = []
        for line in file:
            line.strip()
            _, str_contains_card = line.split(': ')
            win_numbers, game_numbers = str_contains_card.split(' | ')
            win_numbers = list(map(int, win_numbers.split()))
            win_number_qty = 0
            for number in map(int, game_numbers.split()):
                if number in win_numbers:
                    win_number_qty += 1
            if win_number_qty < 2:
                points.append(win_number_qty)
            else:
                points.append(2 ** (win_number_qty - 1))
        
        print(sum(points))

if __name__ == '__main__':
    main()
