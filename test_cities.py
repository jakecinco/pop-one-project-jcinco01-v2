import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    road_map2 = [('Nebraska', 'Lincoln', 40.809868, -96.675345),
                 ('Nevada', 'Carson City', 39.160949, -119.753877),
                 ('New Hampshire', 'Concord', 43.220093, -71.549127),
                 ('New Jersey', 'Trenton', 40.221741, -74.756138)]
    assert compute_total_distance(road_map1) == pytest.approx(9.386 + 18.496 + 10.646, 0.01)
    assert compute_total_distance(road_map2) == pytest.approx(23.1373631 + 48.37535087 + 4.39033418 + 21.9270957, 0.01)


def test_compute_total_distance_is_empty():
    assert compute_total_distance(None) is None  # Pass test 2


def test_swap_cities():
    road_map3 = [("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    road_map3_swapped = [("Minnesota", "Saint Paul", 44.95, -93.094),
                         ("Delaware", "Dover", 39.161921, -75.526755)]
    assert swap_cities(road_map3, 0, 1) == (road_map3_swapped, compute_total_distance(road_map3_swapped))
    assert swap_cities(road_map3, 1, 3) is IndexError
    assert swap_cities(road_map3, 1, 1) is False


def test_shift_cities():
    road_map4 = [1, 2, 3, 4]
    assert shift_cities(road_map4) == 1  # Pass test 4
