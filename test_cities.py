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
    road_map3 = []
    try:
        assert compute_total_distance(road_map1) == pytest.approx(9.386 + 18.496 + 10.646, 0.01)
        assert compute_total_distance(road_map2) == pytest.approx(23.1373631 + 48.37535087 +
                                                                  4.39033418 + 21.9270957, 0.01)
        assert compute_total_distance(None) is None
    except TypeError:
        assert compute_total_distance(["London", 0, 0])
        assert compute_total_distance([0])
        assert compute_total_distance([["London", "England", "0", "0"]])
        assert compute_total_distance()
        assert compute_total_distance(road_map3)


def test_swap_cities():
    empty_road_map = []
    incorrect_road_map = [("Delaware", 39.161921, -75.526755),
                 ("Minnesota", 44.95, -93.094)]
    road_map3 = [("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    road_map3_swapped = [("Minnesota", "Saint Paul", 44.95, -93.094),
                         ("Delaware", "Dover", 39.161921, -75.526755)]
    road_map4 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    road_map4_swapped = [("Minnesota", "Saint Paul", 44.95, -93.094),
                         ("Delaware", "Dover", 39.161921, -75.526755),
                         ("Kentucky", "Frankfort", 38.197274, -84.86311)]
    try:
        assert swap_cities(road_map3, 0, 1) == (road_map3_swapped, compute_total_distance(road_map3_swapped))
        assert swap_cities(road_map4, 0, 2) == (road_map4_swapped, compute_total_distance(road_map4_swapped))
        assert swap_cities(road_map3, 1, 3) is None
    except TypeError:
        assert swap_cities(empty_road_map)
    except ValueError:
        assert swap_cities(incorrect_road_map)


def test_shift_cities():
    road_map5 = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    road_map6 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    try:
        assert shift_cities(road_map5) == [('d', 4), ('a', 1), ('b', 2), ('c', 3)]
        assert shift_cities(road_map6) == [("Minnesota", "Saint Paul", 44.95, -93.094),
                                           ("Kentucky", "Frankfort", 38.197274, -84.86311),
                                           ("Delaware", "Dover", 39.161921, -75.526755)]
        assert shift_cities([('a', 1), ('b', 2)]) == [('b', 2), ('a', 1)]
    except TypeError:
        assert shift_cities()
        assert shift_cities(["London", 0, 0])


def test_convert():
    try:
        assert convert('39.161921') == 39.16
        assert convert('31.1') == 31.1
        assert convert('20') == 20.0
        assert convert('-90') == -90.0
        assert convert(78) == 78.0
        assert convert(53.123412) == 53.12
        assert convert('Delaware') is None
    except ValueError:
        assert convert(39)
        assert convert(120.12)