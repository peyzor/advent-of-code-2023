class Star:
    def __init__(self, position, parts=None):
        self.position = position
        self.parts = parts if parts else []


def main():
    directions = [(-1, -1), (-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, 1), (1, -1)]

    with open('input.txt') as f:
        lines = f.readlines()

    visited = []
    stars = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '*':
                continue

            star = Star(position=(i, j))
            stars.append(star)

            for direction in directions:
                x_dir, y_dir = direction
                x = i + x_dir
                y = j + y_dir
                adj_char = lines[x][y]
                if adj_char.isdigit() and (x, y) not in visited:
                    if 0 <= y + 1 < len(lines[x]) and lines[x][y - 1].isdigit() and lines[x][y + 1].isdigit():
                        search_dir = 1
                        while 0 <= y and lines[x][y].isdigit():
                            y -= 1

                    elif y + 1 < len(lines[x]) and lines[x][y + 1].isdigit():
                        search_dir = 1
                    elif 0 <= y - 1 and lines[x][y - 1].isdigit():
                        search_dir = -1
                    else:
                        star.parts.append(int(adj_char))
                        continue

                    number = ''
                    while (
                            0 <= x < len(lines) and
                            0 <= y < len(lines[x]) and
                            (x, y) not in visited and
                            lines[x][y].isdigit()
                    ):
                        visited.append((x, y))
                        if search_dir == 1:
                            number = number + lines[x][y]
                            y += 1
                        elif search_dir == -1:
                            number = lines[x][y] + number
                            y -= 1

                    if number:
                        star.parts.append(int(number))

    gears = [star.parts for star in stars if len(star.parts) == 2]
    gear_ratios = []
    for gear in gears:
        part1, part2 = gear
        gear_ratio = part1 * part2
        gear_ratios.append(gear_ratio)

    print(sum(gear_ratios))


if __name__ == '__main__':
    main()
