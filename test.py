import unittest

import maze_solver


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
        self.solver = maze_solver.MazeSolver()

    def test_get_starting_cell_returns_starting_cell(self):
        self.assertEqual((0, 0), self.solver.get_starting_cell(SIMPLE_MAZE))

    def test_find_open_cell_returns_adjacent_zero_cell_from_start(self):
        self.assertEqual((0, 1), self.solver.find_open_cell(SIMPLE_MAZE, (0, 0)))


if __name__ == '__main__':
    unittest.main()
