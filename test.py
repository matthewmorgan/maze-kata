from maze_solver import MazeSolver
import unittest


SIMPLE_MAZE = [
    ['S', '0', '1'],
    ['1', '0', '1'],
    ['1', '0', 'E']
]


MODERATE_MAZE = [
    ['S', '0', '0', '1', 'E'],
    ['1', '0', '1', '1', '0'],
    ['1', '0', '0', '1', '0'],
    ['0', '0', '1', '0', '0'],
    ['1', '0', '0', '0', '0']
]


class TestMaze(unittest.TestCase):

    def setUp(self):
        self.maze = MazeSolver()

    def test_can_haz_maze(self):
        assert(isinstance(self.maze, MazeSolver))

    def test_solution_dimensions_match_input_dimensions(self):
        self.assertEquals(len(SIMPLE_MAZE), len(self.maze.solution))

    def test_solution_is_nested_array_of_proper_dimensions(self):
        for idx, line in enumerate(self.maze.solution):
            self.assertTrue(len(line) == len(SIMPLE_MAZE[idx]))

    def test_S_is_replaced_by_x(self):
        for r, row in enumerate(SIMPLE_MAZE):
            for c, cell in enumerate(row):
                if cell == 'S':
                    self.assertEquals(self.maze.solution[r][c], 'x')
                    
    def test_E_is_replaced_by_x(self):
        for r, row in enumerate(SIMPLE_MAZE):
            for c, cell in enumerate(row):
                if cell == 'E':
                    self.assertEquals(self.maze.solution[r][c], 'x')

    def test_no_1_is_replaced_by_x(self):
        for r, row in enumerate(SIMPLE_MAZE):
            for c, cell in enumerate(row):
                if cell == '1':
                    self.assertNotEquals(self.maze.solution[r][c], 'x')

    def test_anything_that_is_not_x_is_1_or_0(self):
        for r, row in enumerate(self.maze.solution):
            for c, cell in enumerate(row):
                if cell != 'x':
                    self.assertTrue(cell in ['1', '0'])

    def test_starting_from_x_you_find_an_adjacent_x(self):
        start_r = 0
        start_c = 0
        for r, row in enumerate(SIMPLE_MAZE):
            for c, cell in enumerate(row):
                if cell == 'S':
                    start_r = r
                    start_c = c
                    self.assertTrue(self.maze.solution[r][c] == 'x')
                    self.assertTrue(self.adjacent_x_exists(r, c))

    def adjacent_x_exists(self, r, c):
        prev_row = r-1
        if prev_row >= 0:
            if self.maze.solution[prev_row][c] == 'x':
                return True
        next_row = r + 1
        if next_row < len(SIMPLE_MAZE):
            if self.maze.solution[next_row][c] == 'x':
                return True
        prev_col = c-1
        if prev_col >= 0:
            if self.maze.solution[r][prev_col] == 'x':
                return True
        next_col = c + 1
        print('next_col: {}'.format(next_col))
        if next_col < len(SIMPLE_MAZE[0]):
            if self.maze.solution[r][next_col] == 'x':
                return True

        return False


        
        

        





if __name__ == '__main__':
    unittest.main()
