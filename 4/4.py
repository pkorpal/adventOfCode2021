from dataclasses import dataclass
import math


@dataclass
class Board:
    id: int
    numbers: list
    rows: list
    cols: list
    score: int

    def __init__(self, numbers, id) -> None:
        self.rows = [[0, 0, 0, 0, 0] for _ in range(5)]
        self.cols = [[0, 0, 0, 0, 0] for _ in range(5)]
        self.numbers = numbers
        self.id = id
        self.score = sum(numbers)
        print(f'Board #{self.id} created: {self}')

    def mark_number(self, number):
        if number in self.numbers:
            self.score -= number
            index = self.numbers.index(number)
            row = math.floor(index/5)
            col = index - row * 5
            self.rows[row][col] = 1
            self.cols[col][row] = 1

    def check_win(self):
        for index in range(5):
            if self.rows[index] == [1, 1, 1, 1, 1] or self.cols[index] == [1, 1, 1, 1, 1]:
                print(f"Board #{self.id} wins")
                return True
        return False
    
    def get_score(self, number):
        print(f'Board #{self.id} score: {self.score * number}')
        


def get_order():
    with open('4_order.txt') as f:
        numbers = f.readlines()[0].split(',')
        return [int(n) for n in numbers if n != '\n']


def get_boards():
    boards = []
    numbers = []
    id = 1
    with open('4_boards.txt') as f:
        for line in f.readlines():
            line = line.replace('\n', '').split(' ')
            for n in line:
                if n != '':
                    numbers.append(int(n))
                if len(numbers) == 25:
                    boards.append(Board(numbers=numbers, id=id))
                    id += 1
                    numbers = []
    return boards


def main():
    order = get_order()
    boards = get_boards()
    winners = []
    loser_id = 0
    for index, number in enumerate(order):
        print(f'#{index}: {number}')
        for board in boards:
            board.mark_number(number)
            if board.check_win() and board.id not in winners:
                winners.append(board.id)
            if len(winners) == len(boards):
                loser_id = board.id
                break
        if len(winners) == len(boards):
            print(f'loser id: {loser_id}')
            boards[loser_id-1].get_score(number)
            break


if __name__ == "__main__":
    main()
