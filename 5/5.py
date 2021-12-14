def get_input(file):
    with open(file) as f:
        coords = []
        for line in f.readlines():
            data = line.replace(' -> ', ',').replace('\n', '').split(',')
            parsed_data = [int(n) for n in data]
            # if parsed_data[0] == parsed_data[2] or parsed_data[1] == parsed_data[3]:
            coords.append(parsed_data)
        return coords


def mark_line(grid, line):
    x1, y1, x2, y2 = line
    # columns
    if x1 == x2:
        x = x1
        y, end = min(y1, y2), max(y1, y2)
        while y <= end:
            if (x, y) in grid.keys():
                grid[(x, y)] += 1
            else:
                grid[(x, y)] = 1
            y += 1
    # rows
    elif y1 == y2:
        y = y1
        x, end = min(x1, x2), max(x1, x2)
        while x <= end:
            if (x, y) in grid.keys():
                grid[(x, y)] += 1
            else:
                grid[(x, y)] = 1
            x += 1
    # diagonal tl - br
    elif x2-x1 == y2-y1:
        y = min(y1, y2)
        x, end = min(x1, x2), max(x1, x2)
        while x <= end:
            if (x, y) in grid.keys():
                grid[(x, y)] += 1
            else:
                grid[(x, y)] = 1
            x += 1
            y += 1
    # diagonal bl - tr
    else:
        y = max(y1, y2)
        x, end = min(x1, x2), max(x1, x2)
        while x <= end:
            if (x, y) in grid.keys():
                grid[(x, y)] += 1
            else:
                grid[(x, y)] = 1
            x += 1
            y -= 1


def get_dangerous_points(grid):
    score = 0
    for _, value in grid.items():
        if value >= 2:
            score += 1
    return score


def main(dev):
    file = ""
    if dev:
        file = 'sample.txt'
    else:
        file = 'input.txt'
    data = get_input(file)
    grid = dict()
    for line in data:
        mark_line(grid, line)
    for key, value in grid.items():
        if value >= 2:
            print(f'{key}: {value}')
    points = get_dangerous_points(grid)
    print(f'Number of dangerous points: {points}')


if __name__ == "__main__":
    main(False)
