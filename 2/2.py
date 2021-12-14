def get_input():
    with open('2_input.txt', 'r') as f:
        return [command.split(' ') for command in f.readlines()]

def get_position(data):
    # part 1
    # horizontal = 0
    # depth = 0
    # for command in data:
    #     if command[0] == 'forward':
    #         horizontal += int(command[1])
    #     elif command[0] == 'up':
    #         depth -= int(command[1])
    #     elif command[0] == 'down':
    #         depth += int(command[1])
    
    # part 2
    horizontal = 0
    depth = 0
    aim = 0
    for command in data:
        if command[0] == 'forward':
            horizontal += int(command[1])
            depth += aim*int(command[1])
        elif command[0] == 'up':
            aim -= int(command[1])
        elif command[0] == 'down':
            aim += int(command[1])
    return horizontal * depth

def main():
    data =  get_input()
    print(get_position(data))

if __name__ == "__main__":
    main()