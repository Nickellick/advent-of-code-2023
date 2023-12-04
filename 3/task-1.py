import io


def find_number(line: str, l_j: int):
    result = line[l_j]
    left_pos = l_j
    right_pos = l_j
    x = l_j + 1
    while x < len(line) and line[x].isdigit():
        result += line[x]
        right_pos = x
        x += 1
    x = l_j - 1
    while x >= 0 and line[x].isdigit():
        result = line[x] + result
        left_pos = x
        x -= 1
    return ((left_pos, right_pos), int(result))
    

def main():
    with open('3/input-1.txt', mode='r') as file:
        SPACER = '.'
        found_partnumbers = []
        found_partnumbers_pos = []
        map = file.readlines()
        for i, line in enumerate(map):
            line = line.strip()
            for j, char_ in enumerate(line):
                if not char_.isdigit() and char_ != SPACER:
                    start_range_i = i - 1
                    stop_range_i = i + 2
                    if i == 0:
                        start_range_i = i
                    if i == len(map) - 1:
                        stop_range_i = i + 1
                    for l_i in range(start_range_i, stop_range_i):
                        start_range_j = j - 1
                        stop_range_j = j + 2
                        if j == 0:
                            start_range_j = j
                        if j == len(line) - 1:
                            stop_range_j = j + 1
                        for l_j in range(start_range_j, stop_range_j):
                            if l_i == i and l_j == j:
                                continue
                            if map[l_i][l_j].isdigit():
                                pos, number = find_number(map[l_i], l_j)
                                l, r = pos
                                h = l_i
                                for pn_pos in found_partnumbers_pos:
                                    pn_l, pn_r, pn_h = pn_pos
                                    if l == pn_l and r == pn_r and h == pn_h:
                                        break
                                else:
                                    found_partnumbers.append(number)
                                    found_partnumbers_pos.append((l, r, h))
        print(sum(found_partnumbers))


if __name__ == '__main__':
    main()
