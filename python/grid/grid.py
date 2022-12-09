"""Generates a grid from 2d array of integers."""


class Grid:
    _grid = None
    points: dict = {}

    def __init__(self, grid):
        self._grid = grid
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                self.points[(y, x)] = cell

    @property
    def width(self):
        return len(self._grid[0])

    @property
    def height(self):
        return len(self._grid)

    def neighbors_left(self, point):
        """Returns a list of points to the left of the given point."""
        y, x = point
        neighbors = []
        for _x in range(x - 1, -1, -1):
            neighbors.append(self.points[(y, _x)])
        return neighbors

    def neighbors_right(self, point):
        """Returns a list of points to the right of the given point."""
        y, x = point
        neighbors = []
        for _x in range(x + 1, self.width):
            neighbors.append(self.points[(y, _x)])
        return neighbors

    def neighbors_top(self, point):
        """Returns a list of points above the given point."""
        y, x = point
        neighbors = []
        for _y in range(y - 1, -1, -1):
            neighbors.append(self.points[(_y, x)])
        return neighbors

    def neighbors_bottom(self, point):
        """Returns a list of points below the given point."""
        y, x = point
        neighbors = []
        for _y in range(y + 1, self.height):
            neighbors.append(self.points[(_y, x)])
        return neighbors
