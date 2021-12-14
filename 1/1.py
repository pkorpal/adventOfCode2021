def get_input():
    with open('1_input.txt', 'r') as f:
        return [int(depth) for depth in f.readlines()]
    
def get_increases(data):
    number_of_increases = 0
    for index in range(len(data)):
        # part 1
        # if index == :
        #     continue
        if index < 4:
            continue
        else:
            # part 1
            # if data[index] > data[index-1]:
            #     number_of_increases += 1
            if data[index] > data[index-3]:
                number_of_increases += 1
    return number_of_increases

def main():
    data = get_input()
    increases = get_increases(data)
    print(increases)

if __name__ == "__main__":
    main()