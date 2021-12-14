def get_input(dev):
    data = []
    if dev:
        with open('sample.txt') as f:
            for line in f.readlines():
                data.append([int(point) for point in line.replace('\n', '')])
            return data
    else:
        with open('input.txt') as f:
            for line in f.readlines():
                data.append([int(point) for point in line.replace('\n', '')])
            return data 
        
def get_low_points(data):
    low_points = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            # check top
            if row > 0  and data[row][col] < data[row-1][col]:
                pass
            elif row == 0:
                pass
            else:
                continue
            # check left
            if col >0 and data[row][col] < data[row][col-1]:
                pass
            elif col == 0:
                pass
            else:
                continue
            # check right
            if col < len(data[row])-1 and data[row][col] < data[row][col+1]:
                pass
            elif col == len(data[row])-1:
                pass
            else:
                continue
            # check bottom
            if row < len(data) -1 and data[row][col] < data[row+1][col]:
                pass
            elif row == len(data) - 1:
                pass
            else:
                continue
            low_points.append((row, col))
    return low_points

def get_risk_level_sum(data, low_points):
    result = 0
    for lp in low_points:
        risk_level = data[lp[0]][lp[1]] +1
        result += risk_level
    return result

def get_basin(data, row, col):
    print(f'row: {row}, col: {col}')
    basin = [(row, col)]
    new_points = []
    print(f'Low point {row,col}, value: {data[row][col]}')
    # top
    if row > 0 and data[row][col] < data[row-1][col]:
        new_points.append((row-1,col))
    # left
    elif col > 0 and data[row][col] < data[row][col-1]:
        new_points.append((row,col-1))
    # right
    elif col < len(data[row]) and data[row][col] < data[row][col+1]:
        new_points.append((row,col+1))
    # bottom
    elif row < len(data) and data[row][col] < data[row+1][col]:
        new_points.append((row+1,col))
    for np in new_points:
        print(np)
        basins = get_basin(data, np[0], np[1])
        for b in basins:
            new_points.append(b)
    for np in new_points:
        basin.append(np)
    return basin

def get_next_point(row, col, data):
    pass
def main():
    debug = True
    data = get_input(debug)
    low_points = get_low_points(data)
    basins = [get_basin(data, lp[0], lp[1]) for lp in low_points]
    print(basins)

if __name__ == "__main__":
    main()