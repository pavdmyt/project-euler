import pytest
from grid import Grid


@pytest.fixture
def ex_grid():
    lst = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]
    return lst


@pytest.fixture
def ref_grid_obj(ex_grid):  # reference grid object
    grid = Grid(0, 0, ex_grid)
    return grid


def test_get_size(ex_grid, ref_grid_obj):
    height = len(ex_grid)
    width = len(ex_grid[0])
    assert (height, width) == ref_grid_obj.get_size()


def test_get_value(ref_grid_obj):
    assert ref_grid_obj.get_value(0, 0) == 1
    assert ref_grid_obj.get_value(1, 1) == 6
    assert ref_grid_obj.get_value(2, 2) == 11


def test_get_right_neighbors(ref_grid_obj):
    result = ref_grid_obj.get_right_neighbors(0, pos=(0, 0))
    assert result == (1,)

    result = ref_grid_obj.get_right_neighbors(1, pos=(1, 1))
    assert result == (6, 7)

    result = ref_grid_obj.get_right_neighbors(2, pos=(2, 1))
    assert result == (10, 11, 12)

    result = ref_grid_obj.get_right_neighbors(3, pos=(2, 1))
    assert result == (10, 11, 12)


def test_get_down_neighbors(ref_grid_obj):
    result = ref_grid_obj.get_down_neighbors(0, pos=(0, 0))
    assert result == (1,)

    result = ref_grid_obj.get_down_neighbors(1, pos=(0, 0))
    assert result == (1, 5)

    result = ref_grid_obj.get_down_neighbors(2, pos=(0, 0))
    assert result == (1, 5, 9)

    result = ref_grid_obj.get_down_neighbors(3, pos=(0, 1))
    assert result == (2, 6, 10)


def test_get_diag_neighbors(ref_grid_obj):
    # position (0, 1)
    result = ref_grid_obj.get_diag_neighbors(0, pos=(0, 1))
    assert result == (2,)

    result = ref_grid_obj.get_diag_neighbors(1, pos=(0, 1))
    assert result == (2, 7)

    result = ref_grid_obj.get_diag_neighbors(2, pos=(0, 1))
    assert result == (2, 7, 12)

    result = ref_grid_obj.get_diag_neighbors(3, pos=(0, 1))
    assert result == (2, 7, 12)

    # position (0, 2)
    result = ref_grid_obj.get_diag_neighbors(0, pos=(0, 2))
    assert result == (3,)

    result = ref_grid_obj.get_diag_neighbors(1, pos=(0, 2))
    assert result == (3, 8)

    result = ref_grid_obj.get_diag_neighbors(2, pos=(0, 2))
    assert result == (3, 8)
