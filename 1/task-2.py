def main():
    text = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    with open('1/input-2.txt', mode='r') as file:
        result = 0
        for line in file:
            total_num = ''
            digit_num = ''
            literal_num = ''
            left_word_pos = None
            left_digit_pos = None
            right_word_pos = None
            right_digit_pos = None
            is_break = False
            for pos, char_ in enumerate(line):
                if is_break:
                    break
                if char_.isdigit():
                    digit_num += char_
                    left_digit_pos = pos
                    break
                for word, value in text.items():
                    if word == line[pos:pos+len(word)]:
                        literal_num += value
                        left_word_pos = pos
                        is_break = True
                        break
            is_break = False
            for pos, char_ in enumerate(line[::-1]):
                if is_break:
                    break
                if char_.isdigit():
                    digit_num += char_
                    right_digit_pos = len(line) - pos - 1
                    break
                for word, value in text.items():
                    if word == line[len(line) - pos - len(word):len(line) - pos]:
                        literal_num += value
                        right_word_pos = len(line) - pos - 1
                        is_break = True
                        break
            if len(literal_num) == 1:
                if left_word_pos is not None:
                    right_word_pos = left_word_pos
                else:
                    left_word_pos = right_word_pos
            if len(digit_num) == 1:
                if left_digit_pos is not None:
                    right_digit_pos = left_digit_pos
                else:
                    left_digit_pos = right_digit_pos
            
            if left_digit_pos is None:
                total_num += literal_num[0] + (literal_num[1] if len(literal_num) > 1 else literal_num[0])
            elif left_word_pos is None:
                total_num += digit_num[0] + (digit_num[1] if len(digit_num) > 1 else digit_num[0])
            else:
                if left_word_pos < left_digit_pos:
                    total_num += literal_num[0]
                else:
                    total_num += digit_num[0]
                if right_word_pos > right_digit_pos:
                    total_num += literal_num[1] if len(literal_num) > 1 else literal_num[0]
                else:
                    total_num += digit_num[1] if len(digit_num) > 1 else digit_num[0]

            result += int(total_num)
        print(result)


if __name__ == '__main__':
    main()
