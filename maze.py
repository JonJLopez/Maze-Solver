from cell import Cell
import time
import random

class Maze():
    def __init__(
            self,
            x1, y1,
            num_rows, num_cols,
            cell_size_x, cell_size_y,
            win,
            seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        if seed is not None:
            random.seed(seed)
    
    def _create_cells(self):
        self._cells = [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
        if self._num_cols > 0 and self._num_rows > 0:
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)
        
    
    def _draw_cell(self, i, j):
        if self._win is None or self._num_cols < 1 or self._num_rows < 1:
            return
        x1 = self._cell_size_x*i + self._x1
        y1 = self._cell_size_y*j + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while 1:
            to_visit = []
            # left
            if i > 0 and not self._cells[i-1][j]._visited:
                to_visit.append((i-1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i+1][j]._visited:
                to_visit.append((i+1, j))
            # above
            if j > 0 and not self._cells[i][j-1]._visited:
                to_visit.append((i, j-1))
            # below
            if j < self._num_rows - 1 and not self._cells[i][j+1]._visited:
                to_visit.append((i, j+1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            direction = to_visit[random.randrange(0, len(to_visit))]
            d_i = direction[0]
            d_j = direction[1]
            # left
            if i - 1 == direction[0]:
                self._cells[d_i][d_j].has_right_wall = False
                self._cells[i][j].has_left_wall = False
            # right
            if i + 1 == direction[0]:
                self._cells[d_i][d_j].has_left_wall = False
                self._cells[i][j].has_right_wall = False
            # above
            if j - 1 == direction[1]:
                self._cells[d_i][d_j].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False
            # below
            if j + 1 == direction[0]:
                self._cells[d_i][d_j].has_top_wall = False
                self._cells[i][j].has_top_wall = False
            self._break_walls_r(d_i, d_j)

            
