import pytest
from cities import *
from tk import *


def test_convert_coordinates():
    road_map1 = [('Oklahoma', 'Oklahoma City', '35.482309', '-97.534994'), 0]
    assert convert_coordinates(road_map1[0]) == ('Oklahoma', 'Oklahoma City', 35, -97)

