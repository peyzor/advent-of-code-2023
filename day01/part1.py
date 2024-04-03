def main():
    results = []

    with open('input.txt') as f:
        lines = f.readlines()
        digits = []
        for line in lines:
            for char in line:
                if char.isdigit():
                    digits.append(char)

            results.append(int(digits[0] + digits[-1]))
            digits = []

        print(sum(results))


if __name__ == '__main__':
    main()
