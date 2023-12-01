def main():
    with open('1/input-1.txt', mode='r') as file:
        result = 0
        for line in file:
            num = ''
            left_pos = 0
            for pos, char_ in enumerate(line):
                if char_.isdigit():
                    num += char_
                    left_pos = pos
                    break
            for pos, char_ in enumerate(line[::-1]):
                if char_.isdigit():
                    num += char_
                    break
            result += int(num)
        print(result)


if __name__ == '__main__':
    main()
