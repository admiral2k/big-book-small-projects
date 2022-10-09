from random import randint
from time import sleep
from os import system


class GameOfLife:
    ALIVE = '0'
    DEAD = ' '

    def __init__(self, width, length):
        if length > 0 and width > 0:
            self._width = width
            self._length = length
            self._currentCells = {}
            self.randomly_fill()
        else:
            raise ValueError("Wrong size input.")

    def __str__(self):
        output = ""
        for y in range(self._length):
            for x in range(self._width):
                output += self._currentCells[(x, y)]
            output += "\n"
        return output

    def randomly_fill(self):
        for x in range(self._width):
            for y in range(self._length):
                if randint(0,1):
                    self._currentCells[(x, y)] = self.ALIVE
                else:
                    self._currentCells[(x, y)] = self.DEAD

    def tick(self):
        next_cells={}
        for x in range(self._width):
            for y in range(self._length):
                right = (x - 1) % self._width
                left = (x + 1) % self._width
                up = (y - 1) % self._length
                down = (y + 1) % self._length

                num_of_neighbors = 0
                if self._currentCells[(left, y)] == self.ALIVE:
                    num_of_neighbors += 1

                if self._currentCells[(left, up)] == self.ALIVE:
                    num_of_neighbors += 1

                if self._currentCells[(x, up)] == self.ALIVE:
                    num_of_neighbors += 1

                if self._currentCells[(right, up)] == self.ALIVE:
                    num_of_neighbors += 1

                if self._currentCells[(right, y)] == self.ALIVE:
                    num_of_neighbors += 1

                if self._currentCells[(right, down)] == self.ALIVE:
                    num_of_neighbors += 1

                if self._currentCells[(x, down)] == self.ALIVE:
                    num_of_neighbors += 1

                if self._currentCells[(left, down)] == self.ALIVE:
                    num_of_neighbors += 1

                if num_of_neighbors in [2, 3] and self._currentCells[(x, y)] == self.ALIVE:
                    next_cells[(x, y)] = self.ALIVE
                elif num_of_neighbors == 3 and self._currentCells[(x, y)] == self.DEAD:
                    next_cells[(x, y)] = self.ALIVE
                else:
                    next_cells[(x, y)] = self.DEAD
        self._currentCells = next_cells

def main():
    game = GameOfLife(140, 30)
    while True:
        try:
            system("cls")
            print(game)
            print("Press ctrl + C to stop the game.")
            game.tick()
            sleep(0.1)
        except KeyboardInterrupt:
            system("cls")
            print(game)
            print("Created by Amir @admiral2k.")
            break


if __name__ == "__main__":
    main()
