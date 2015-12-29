"""
Grid class.
"""


class Grid:
    """
    Grid object with methods to get neighbor values.
    """
    def __init__(self, height, width, export_grid=None):
        if export_grid:
            self._grid = [[col for col in row] for row in export_grid]
        # empty grid.
        else:
            self._grid = [[[] for col in range(width)]
                          for row in range(height)]

        self._height = len(self._grid)
        self._width = len(self._grid[0])

    def __repr__(self):
        res = [str(row) for row in self._grid]
        return '\n'.join(res)

    def get_size(self):
        """
        Return grid size.
        """
        return self._height, self._width

    def get_value(self, row, col):
        """
        Return value of the currently selected cell.
        """
        return self._grid[row][col]

    def get_right_neighbors(self, qty, pos):
        """
        Return tuple with current position value and specified
        qty of the neighbors to the right.
        """
        height, width = pos
        qty += 1
        if qty:
            res_lst = self._grid[height][width: width + qty]
            return tuple(res_lst)
        return ()

    def get_down_neighbors(self, qty, pos):
        """
        Return tuple with current position value and specified
        qty of the downward neighbors.
        """
        height, width = pos
        col_vals = [row[width] for row in self._grid[height:]]
        qty += 1
        if qty:
            res_lst = col_vals[:qty]
            return tuple(res_lst)
        return ()

    def get_diag_neighbors(self, qty, pos, mode='right'):
        """
        Return tuple with current position value and specified
        qty of the downward diagonal right or left neighbors.
        """
        height, width = pos
        diag_vals = []
        offset = 0
        for row in self._grid[height:]:
            diag_vals.append(row[width + offset])
            if mode == 'right':
                offset += 1
                if offset >= self._width - width:
                    break
            elif mode == 'left':
                offset -= 1
                if -offset > width:
                    break
            else:
                return ()

        qty += 1
        if qty:
            res_lst = diag_vals[:qty]
            return tuple(res_lst)
        return ()
