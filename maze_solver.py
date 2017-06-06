class MazeSolver:
    def __init__(self):
        pass

    def get_starting_cell(self, maze):
        for row_index, row in enumerate(maze):
            for cell_index, cell in enumerate(row):
                if cell == 'S':
                    return row_index, cell_index

    def find_open_cell(self, maze, occupied_cell):
        if maze[occupied_cell[0]][occupied_cell[1]+1] == '0':
            return occupied_cell[0], occupied_cell[1]+1
        else:
            return occupied_cell[0]+1, occupied_cell[1]

