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

    def test_solution_is_nested_array(self):
        for line in self.maze.solution:
            self.assertTrue(len(line) == len(SIMPLE_MAZE[0]))
        

        





if __name__ == '__main__':
    unittest.main()
