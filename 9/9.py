from time import perf_counter

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
            if data[row][col] == 9:
                continue
            neighbours = []
            if row > 0:
                neighbours.append(data[row-1][col])
            if row < len(data)-1:
                neighbours.append(data[row+1][col])
            if col > 0:
                neighbours.append(data[row][col-1])
            if col < len(data[row])-1:
                neighbours.append(data[row][col+1])
            if data[row][col] < min(neighbours):
                low_points.append((row,col))
            
            # check top

            # if row > 0  and data[row][col] < data[row-1][col]:
            #     pass
            # elif row == 0:
            #     pass
            # else:
            #     continue
            # # check left
            # if col >0 and data[row][col] < data[row][col-1]:
            #     pass
            # elif col == 0:
            #     pass
            # else:
            #     continue
            # # check right
            # if col < len(data[row])-1 and data[row][col] < data[row][col+1]:
            #     pass
            # elif col == len(data[row])-1:
            #     pass
            # else:
            #     continue
            # # check bottom
            # if row < len(data) -1 and data[row][col] < data[row+1][col]:
            #     pass
            # elif row == len(data) - 1:
            #     pass
            # else:
            #     continue
            # low_points.append((row, col))
    print(low_points)
    return low_points

def get_risk_level_sum(data, low_points):
    result = 0
    for lp in low_points:
        risk_level = data[lp[0]][lp[1]] +1
        result += risk_level
    return result

def get_basin(data, row, col):
    basin = [(row, col)]
    new_points = []
    print(f'Low point {row,col}, value: {data[row][col]}')
    # top
    if 0 < row < len(data)-1 and data[row][col] < data[row-1][col] and data[row-1][col] != 9:
        new_points.append((row-1,col))
    # left
    if 0 < col < len(data[row])-1 and data[row][col] < data[row][col-1] and data[row][col-1] != 9: 
        new_points.append((row,col-1))
    # right
    if 0 < col < len(data[row])-1 and data[row][col] < data[row][col+1] and data[row][col+1] != 9:
        new_points.append((row,col+1))
    # bottom
    if 0 < row < len(data)-1 and data[row][col] < data[row+1][col] and data[row+1][col] != 9:
        new_points.append((row+1,col))
    print(f'new points: {new_points}')
    for np in new_points:
        basin.append(np)
    return basin

def get_next_point(row, col, data):
    pass

def main():
    debug = False
    data = get_input(debug)
    t0 = perf_counter()
    for _ in range(1000):
        low_points = get_low_points(data)
    t = perf_counter()
    print(f'Elapsed time: {t-t0}')
    # basins = [get_basin(data, lp[0], lp[1]) for lp in low_points]
    # for basin in basins:
    #     print(basin)

if __name__ == "__main__":
    main()