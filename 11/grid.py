"""
Grid class.
"""

class Grid:
    # !!!TODO: align `h, w` to `pos_h, pos_w` where appropriate.
    def __init__(self, height, width, export_grid=None):
        if export_grid:
            # !!!TODO: make CLONE here.
            self._grid = export_grid
        else:
            self._grid = [[[] for col in range(width)] for row in range(height)]

        self._height = len(self._grid)
        self._width = len(self._grid[0])
        self._moves_done = 0  # required for looping over the grid.
        # Current position in the grid (selected cell).
        self._cur_position = {'height': 0, 'width': 0}
        # self._flat_grid = [item for row in self._grid for item in row]

    def __repr__(self):
        res = [str(row) for row in self._grid]
        return '\n'.join(res)

    def get_size(self):
        """
        Return (grid.height, grid.width).
        """
        return self._height, self._width

    def get_cur_position(self):
        """
        Return coordinates with currently selected cell.
        """
        return self._cur_position['height'], self._cur_position['width']

    def get_value(self):
        """
        Return value of the currently selected cell.
        """
        h, w = self.get_cur_position()
        return self._grid[h][w]

    def _move_forward(self):
        h, w = self.get_cur_position()
        if w == self._width - 1:
            # Last item in the grid.
            if h == self._height - 1:
                return self.get_cur_position()
            else:
                self._cur_position['height'] += 1
                self._cur_position['width'] = 0
        else:
            self._cur_position['width'] += 1
        return self.get_cur_position()

    def next(self):
        value = self.get_value()
        self._move_forward()
        self._moves_done += 1
        h, w = self.get_size()
        if self._moves_done == (h * w) + 1:
            # Clear values for the next usage.
            self._moves_done = 0
            self._cur_position['height'] = 0
            self._cur_position['width'] = 0
            raise StopIteration
        return value

    def __iter__(self):
        return self

    # !!!TODO: consider moving `get_neighbors` methods into
    #          separate class.
    def get_right_neighbors(self, qty):
        """
        Returns current position value + specified qty of the
        neighbors to the right.
        """
        pos_h, pos_w = self.get_cur_position()
        qty += 1
        if qty:
            res_lst = self._grid[pos_h][pos_w: pos_w+qty]
            return tuple(res_lst)
        return ()

    def get_down_neighbors(self, qty):
        """
        Returns current position value + specified qty of the
        downward neighbors.
        """
        pos_h, pos_w = self.get_cur_position()
        col_vals = [row[pos_w] for row in self._grid[pos_h:]]
        qty += 1
        if qty:
            res_lst = col_vals[:qty]
            return tuple(res_lst)
        return ()

    def get_diag_neighbors(self, qty):
        """
        Returns current position value + specified qty of the
        downward diagonal right neighbors.
        """
        pos_h, pos_w = self.get_cur_position()
        diag_vals = []
        offset = 0
        for row in self._grid[pos_h:]:
            diag_vals.append(row[pos_w + offset])
            offset += 1
        qty += 1
        if qty:
            res_lst = diag_vals[:qty]
            return tuple(res_lst)
        return ()
