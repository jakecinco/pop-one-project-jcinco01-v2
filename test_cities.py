import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311), \
                 ("Delaware", "Dover", 39.161921, -75.526755), \
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert compute_total_distance(road_map1) == \
           pytest.approx(9.386 + 18.496 + 10.646, 0.01)


def test_compute_total_distance2():
    road_map1 = [1, 2, 3, 4]
    assert compute_total_distance(road_map1) == road_map1 + road_map1  # Pass test 1


def test_compute_total_distance3():
    road_map2 = []
    assert compute_total_distance(road_map2) is None  # Pass test 2


def test_swap_cities():
    road_map3 = [("Delaware", "Dover", 39.161921, -75.526755), \
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    road_map3_swapped = [("Minnesota", "Saint Paul", 44.95, -93.094), \
                        ("Delaware", "Dover", 39.161921, -75.526755)]
    assert swap_cities(road_map3, 1, 1) != road_map3_swapped  # Pass test 3


def test_shift_cities():
    road_map4 = [1, 2, 3, 4]
    assert shift_cities(road_map4) == 1  # Pass test 4
