def main():
    result = 0
    numbers_map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    with open('inputx.txt') as f:
        lines = f.readlines()
        for line in lines:
            digits = []
            seen_positions = []

            left, right = 0, 0
            for i in range(len(line)):
                right = i + 1

                if line[i].isdigit():
                    digits.append(line[i])
                    left = right
                    continue

                for num, v in numbers_map.items():
                    found_pos = line.find(num, left, right + 1)
                    seen_coordinate = (num, found_pos)
                    if found_pos != -1 and seen_coordinate not in seen_positions:
                        digits.append(str(v))
                        seen_positions.append(seen_coordinate)
                        left = right

            result += int(digits[0] + digits[-1])

        print(result)


if __name__ == '__main__':
    main()
