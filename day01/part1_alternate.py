def main():
    output = 0

    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            count = 0
            first = None
            last = None
            for char in line:
                if char.isdigit():
                    count += 1
                    if count == 1:
                        first, last = char, char
                    else:
                        last = char

            output += int(first + last)

        print(output)


if __name__ == '__main__':
    main()
