class MazeSolver:
    def __init__(self):
        pass

    def get_starting_cell(self, maze):
        for row_index, row in enumerate(maze):
            for cell_index, cell in enumerate(row):
                if cell == 'S':
                    return row_index, cell_index
