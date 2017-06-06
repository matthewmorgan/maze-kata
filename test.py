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

    def test_can_haz_maze(self):
        solver = MazeSolver()
        self.assertEquals(isinstance(solver.solve(SIMPLE_MAZE), list), True)
    
    def test_solved_maze_is_proper_size(self):
        solver = MazeSolver()
        self.assertEquals(len(solver.solve(SIMPLE_MAZE)), len(SIMPLE_MAZE))

    def test_check_elements_S(self):
        solver = MazeSolver()
        solution = solver.solve(SIMPLE_MAZE)
        for row in solution:
            for col in row:
                self.assertNotEquals(col, 'S')

    def test_check_elements_E(self):
        solver = MazeSolver()
        solution = solver.solve(SIMPLE_MAZE)
        for row in solution:
            for col in row:
                self.assertNotEquals(col, 'E')

    def test_start_at_start(self):
        solver = MazeSolver()
        solution = solver.solve(SIMPLE_MAZE)
        self.assertEquals(solution[0][0], 'x')

    
        



if __name__ == '__main__':
    unittest.main()
