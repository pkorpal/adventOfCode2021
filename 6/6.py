def get_input(dev):
    if dev:
        with open('1.txt') as f:
            return [int(n) for n in f.readlines()[0].replace('\n', 'n').split(',')]
    else:
        with open('input.txt') as f:
            return [int(n) for n in f.readlines()[0].replace('\n', 'n').split(',')]
        
def get_final_fish_count(fish, num_of_days):
    for i in range(num_of_days):
        print(f'Day #{i} - {fish}')
        new_fish_this_day = []
        for index, f in enumerate(fish):
            if f == 0:
                fish[index] = 6
                new_fish_this_day.append(8)
            else:
                fish[index] -= 1
        for f in new_fish_this_day:
            fish.append(f)
    return len(fish)

def main():
    data = get_input(True)
    print(get_final_fish_count(data, 80))

if __name__ == "__main__":
    main()