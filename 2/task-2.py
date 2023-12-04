def main():
    with open('2/input-1.txt', mode='r') as file:
        result = 0
        for line in file:
            line.strip()
            str_contains_id, str_contains_game = line.split(': ')
            max_red = 0
            max_green = 0
            max_blue = 0
            for reveal in str_contains_game.split('; '):
                for cubes in reveal.split(', '):
                    qty, name = cubes.split()
                    if name == 'red':
                        max_red = max_red if int(qty) < max_red else int(qty)
                    if name == 'green':
                        max_green = max_green if int(qty) < max_green else int(qty)
                    if name == 'blue':
                        max_blue = max_blue if int(qty) < max_blue else int(qty)
            result += max_red * max_green * max_blue
        print(result)


if __name__ == '__main__':
    main()
