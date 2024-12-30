import unittest
from maze import Maze
from graphics import Window
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_0_cells(self):
        num_cols = 0
        num_rows = 0
        win = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
           m1._cells[num_cols-1][num_rows-1].has_bottom_wall,
           False,
        )

    def test_maze_reset_cells_visited(self):
        num_cols = 4
        num_rows = 4
        win = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(m1._cells[i][j]._visited, False)
if __name__ == "__main__":
    unittest.main()