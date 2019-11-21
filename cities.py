import copy
import math
import random
import os.path


def read_cities(file_name):
    with open(file_name, "r") as file:
        lines = file.read().splitlines()
        cities = [tuple(line.split("\t")) for line in lines]
        return cities


def convert(num):  # Print only one or two digits after the decimal point
    return float("{0:.2f}".format(float(num)))


def print_cities(road_map):
    road_map = read_cities(road_map)
    # print([(city[1], convert(city[2]), convert(city[3])) for city in road_map])
    x = [(city[1], convert(city[2]), convert(city[3])) for city in road_map]
    for city in x:
        print(city)


def compute_total_distance(road_map):
    if not road_map:
        return None
    else:
        road_map_copy = copy.deepcopy(road_map)
        road_map_copy.append(road_map[0])
        # road_map_copy = [(city[1], convert(city[2]), convert(city[3])) for city in road_map_copy]
        total_distance = 0.0
        for i in range(len(road_map_copy) - 1):
            lats = float(road_map_copy[i][2]) - float(road_map_copy[i + 1][2])
            longs = float(road_map_copy[i][3]) - float(road_map_copy[i + 1][3])
            distance = math.sqrt(lats ** 2 + longs ** 2)
            total_distance += distance
    return convert(total_distance)


def swap_cities(road_map, index1, index2):
    try:
        while index1 == index2:
            index1 = random.randint(0, len(road_map)-1)
        road_map[index1], road_map[index2] = road_map[index2], road_map[index1]
        new_total_distance = compute_total_distance(road_map)
        return road_map, new_total_distance

    except IndexError or None:
        print("Index out of range")


def shift_cities(road_map):
    new_road_map = [road_map[-1]]
    new_road_map.extend(road_map[:-1])
    return new_road_map


def find_best_cycle(road_map):
    best_cycle_total = compute_total_distance(road_map)
    best_cycle = ()
    for i in range(10000):
        road_map = shift_cities(road_map)
        best_found = swap_cities(road_map, random.randint(0, len(road_map))-1, random.randint(0, len(road_map)-1))
        if best_found[1] < best_cycle_total:
            best_cycle_total = best_found[1]
            best_cycle = best_found
    return best_cycle


def print_map(road_map):
    road_map = read_cities(road_map)
    road_map.append(road_map[0])
    for i in range(len(road_map) - 1):
        cityA = road_map[i]
        cityB = road_map[i + 1]
        distance = math.sqrt((float(cityA[2]) - float(cityB[2])) ** 2 + (float(cityA[3]) - float(cityB[3])) ** 2)
        print(f"{cityA[1]} -----> {cityB[1]} ===== {convert(distance)}")
    print(f"Total distance: {convert(compute_total_distance(road_map))}")


def main():
    file = input()  # Code file input validation here - make sure the file exists and valid
    if os.path.isfile(file) is True:
        print_cities(file)
        print_map(file)
        print(find_best_cycle(read_cities(file)))
    else:
        print("Input file does not exist")


if __name__ == "__main__":  # keep this in
    main()
