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
        

if __name__ == '__main__':
    unittest.main()
