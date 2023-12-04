def main():
    with open('2/input-1.txt', mode='r') as file:
        MAX_RED = 12
        MAX_GREEN = 13
        MAX_BLUE = 14
        result = 0
        for line in file:
            is_possible = True
            line.strip()
            str_contains_id, str_contains_game = line.split(': ')
            id_ = int(str_contains_id.split()[1])
            for reveal in str_contains_game.split('; '):
                red = 0
                green = 0
                blue = 0
                for cubes in reveal.split(', '):
                    qty, name = cubes.split()
                    if name == 'red':
                        red += int(qty)
                    if name == 'green':
                        green += int(qty)
                    if name == 'blue':
                        blue += int(qty)
                if red > MAX_RED or green > MAX_GREEN or blue > MAX_BLUE:
                    is_possible = False
                    break
            if is_possible:
                result += id_
        print(result)


if __name__ == '__main__':
    main()
