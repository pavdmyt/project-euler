"""
Grid class.
"""


class Grid:
    # !!!TODO: align `h, w` to `row, col` where appropriate.
    def __init__(self, height, width, export_grid=None):
        if export_grid:
            # !!!TODO: make CLONE here.
            self._grid = export_grid
        else:
            self._grid = [[[] for col in range(width)]
                          for row in range(height)]

        self._height = len(self._grid)
        self._width = len(self._grid[0])
        self._moves_done = 0  # required for looping over the grid.
        self._flat_grid = [item for row in self._grid for item in row]

    def __repr__(self):
        res = [str(row) for row in self._grid]
        return '\n'.join(res)

    def get_size(self):
        """
        Return (grid.height, grid.width).
        """
        return self._height, self._width

    def get_value(self, row, col):
        """
        Return value of the currently selected cell.
        """
        return self._grid[row][col]

    # !!!TODO: consider moving `get_neighbors` methods into
    #          separate class.
    def get_right_neighbors(self, qty, pos):
        """
        Returns current position value + specified qty of the
        neighbors to the right.
        """
        row, col = pos
        qty += 1
        if qty:
            res_lst = self._grid[row][col : col + qty]
            return tuple(res_lst)
        return ()

    def get_down_neighbors(self, qty, pos):
        """
        Returns current position value + specified qty of the
        downward neighbors.
        """
        row, col = pos
        col_vals = [row[col] for row in self._grid[row:]]
        qty += 1
        if qty:
            res_lst = col_vals[:qty]
            return tuple(res_lst)
        return ()

    def get_diag_neighbors(self, qty, pos):
        """
        Returns current position value + specified qty of the
        downward diagonal right neighbors.
        """
        row, col = pos
        diag_vals = []
        offset = 0
        for row in self._grid[row:]:
            diag_vals.append(row[col + offset])
            offset += 1
        qty += 1
        if qty:
            res_lst = diag_vals[:qty]
            return tuple(res_lst)
        return ()
