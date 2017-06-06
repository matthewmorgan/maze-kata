from copy import deepcopy


class MazeSolver:
    def __init__(self):
        pass

    def get_starting_cell(self, maze):
        for row_index, row in enumerate(maze):
            for cell_index, cell in enumerate(row):
                if cell == 'S':
                    return row_index, cell_index

    def find_open_cell(self, maze, occupied_cell):
        if maze[occupied_cell[0]][occupied_cell[1] + 1] == '0':
            return occupied_cell[0], occupied_cell[1] + 1
        else:
            return occupied_cell[0] + 1, occupied_cell[1]

    def move_forward_in_maze(self, maze, occupied_cell):
        new_maze = deepcopy(maze)
        new_maze[occupied_cell[0]][occupied_cell[1]] = 'x'
        new_cell = self.find_open_cell(new_maze, occupied_cell)
        new_maze[new_cell[0]][new_cell[1]] = 'x'
        return new_maze, new_cell

    def solve_maze(self, maze):
        next_cell = self.get_starting_cell(maze)
        new_maze = deepcopy(maze)

        while True:
            new_maze, next_cell = self.move_forward_in_maze(new_maze, next_cell)
