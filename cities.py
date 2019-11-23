import copy
import math
import random
import os.path


def read_cities(file_name):
    with open(file_name, "r") as file:
        lines = file.read().splitlines()
        cities = [tuple(line.split("\t")) for line in lines]
        return cities


def convert(num):  # Convert string to 2-decimal place float
    try:
        return float("{0:.2f}".format(float(num)))
    except ValueError:
        print("Cannot convert non-numerical strings to float.")


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
            distance = math.sqrt(lats * lats + longs * longs)
            total_distance += distance
    return convert(total_distance)


def swap_cities(road_map, index1, index2):
    try:
        while index1 == index2:
            index1 = random.randint(0, len(road_map) - 1)
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
        shift_cities(road_map)
        swapped = swap_cities(road_map, random.randint(0, len(road_map)) - 1, random.randint(0, len(road_map) - 1))
        if swapped[1] < best_cycle_total:
            best_cycle_total = swapped[1]
            best_cycle = swapped
    return best_cycle


def print_map(road_map):
    road_map = read_cities(road_map)
    road_map.append(road_map[0])
    for i in range(len(road_map) - 1):
        cityA = road_map[i]
        cityB = road_map[i + 1]
        distance = math.sqrt((float(cityA[2]) - float(cityB[2])) ** 2 + (float(cityA[3]) - float(cityB[3])) ** 2)
        print(f"{cityA[0]} -----> {cityB[0]} ===== {convert(distance)}")
    print(f"Total distance: {convert(compute_total_distance(road_map))}")


def draw_map(road_map):
    lats = [convert(city[2]) for city in road_map]
    longs = [convert(city[3]) for city in road_map]
    min_lats = min(lats)
    max_lats = max(lats)
    min_longs = min(longs)
    max_longs = max(longs)
    coor = int(min_lats), int(max_lats), int(min_longs), int(max_longs)
    for x in range(coor[2], coor[3] + 1, 5):
        print("\t" + str(x), end="")
    print(end="\n")
    for y in range(coor[1], coor[0] + 1, -5):
        for i in range(0, abs(coor[2]) - abs(coor[3]), 5):
            print("\t" + " | ", end="")
        print(end="\n")
        print(y, end="")
        for j in range(0, abs(coor[2]) - abs(coor[3]), 5):
            print("    " + "-" + "\t", end="")
        print(end="\n")


# def visualise():

def main():
    file = input()
    if os.path.isfile(file):
        print_cities(file)
        print_map(file)
        print(find_best_cycle(read_cities(file)))
        draw_map(read_cities(file))
    else:
        print("Input file does not exist. Enter correct file name.")


if __name__ == "__main__":  # keep this in
    main()
