def get_input():
    with open('3_input.txt') as f:
        return [bn.replace('\n', '') for bn in f.readlines()]
    
def get_2_to_power_n(index):
    result = 1
    for _ in range(int(index)):
        result = result * 2
    return result

    
def get_power_consumption(data):
    gamma_rate = [[0,0] for _ in range(len(data[0]))]
    for reading in data:
        for index, number in enumerate(reading):
            if number == '0':
                gamma_rate[index][0] +=1
            else:
                gamma_rate[index][1] +=1
    gr = ''
    er = ''
    for reading in gamma_rate:
        if reading[0] > reading[1]:
            gr += '0'
            er += '1'
        else:
            gr += '1'
            er += '0'
    gr_value = sum([get_2_to_power_n(len(gr) - index - 1) * int(value) for index, value in enumerate(gr)])
    er_value = sum([get_2_to_power_n(len(gr) - index - 1) * int(value) for index, value in enumerate(er)])
    return gr_value * er_value

def main():
    data = get_input()
    print(get_power_consumption(data))

if __name__ == "__main__":
    main()
