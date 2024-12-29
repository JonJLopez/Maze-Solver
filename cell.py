from graphics import Line, Point, Window

class Cell():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            wall = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(wall)
        if self.has_right_wall:
            wall = Line(Point(x2, y2), Point(x2, y1))
            self._win.draw_line(wall)
        if self.has_top_wall:
            wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(wall)
        if self.has_bottom_wall:
            wall = Line(Point(x2, y2), Point(x1, y2))
            self._win.draw_line(wall)
        
    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        
        p1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        p2 = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        connecting_line = Line(p1, p2)
        self._win.draw_line(connecting_line, fill_color)