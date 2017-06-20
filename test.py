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
        self.assertEquals(3, len(self.maze.solution))
        





if __name__ == '__main__':
    unittest.main()
