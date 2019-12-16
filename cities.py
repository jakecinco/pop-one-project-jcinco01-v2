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
    cities = [(city[0], city[1], convert(city[2]), convert(city[3])) for city in road_map]
    for city in cities:
        print(city)
    # print([(city[1], convert(city[2]), convert(city[3])) for city in road_map]) # --> prints list of cities in 1 line


def compute_total_distance(road_map):
    if not road_map:
        return None
    else:
        map_copy = [*road_map]
        map_copy.append(road_map[0])
        total_distance = 0.0
        for i in range(len(map_copy) - 1):
            lats = float(map_copy[i][2]) - float(map_copy[i + 1][2])
            longs = float(map_copy[i][3]) - float(map_copy[i + 1][3])
            distance = math.sqrt(lats * lats + longs * longs)
            total_distance += distance
    return convert(total_distance)


def swap_cities(road_map, index1, index2):
    try:
        map_copy = road_map[:]
        while index1 == index2:
            index1 = random.randint(0, len(map_copy) - 1)
            index2 = random.randint(0, len(map_copy) - 1)
        map_copy[index1], map_copy[index2] = map_copy[index2], map_copy[index1]
        new_total_distance = compute_total_distance(map_copy)
        return map_copy, new_total_distance
    except IndexError or None:
        print("Index out of range")


def shift_cities(road_map):
    new_road_map = [road_map[-1]]
    new_road_map.extend(road_map[:-1])
    return new_road_map


def find_best_cycle(road_map):
    best_cycle_total = compute_total_distance(road_map)
    best_cycle = [*road_map]
    for i in range(10000):
        index1 = random.randint(0, len(road_map) - 1)
        index2 = random.randint(0, len(road_map) - 1)
        best_cycle = shift_cities(best_cycle)
        new_road_map, new_total_distance = swap_cities(best_cycle, index1, index2)
        if new_total_distance < best_cycle_total:
            best_cycle_total = new_total_distance
            best_cycle = new_road_map
    return best_cycle


def print_map(road_map):
    map_copy = road_map[:]
    map_copy.append(road_map[0])
    for i in range(len(map_copy) - 1):
        cityA = map_copy[i]
        cityB = map_copy[i + 1]
        distance = math.sqrt((float(cityA[2]) - float(cityB[2])) ** 2 + (float(cityA[3]) - float(cityB[3])) ** 2)
        print(f"{cityA[0]} -----> {cityB[0]} ===== {convert(distance)}")
    print(f"Total distance: {convert(compute_total_distance(map_copy))}")


def visualise(road_map):
    lats = [int(float(city[2])) for city in road_map]
    longs = [int(float(city[3]))for city in road_map]
    cities = [(city[0], int(float(city[2])), int(float(city[3]))) for city in road_map]
    min_lats = min(lats)
    max_lats = max(lats)
    min_longs = min(longs)
    max_longs = max(longs)
    columns = ""
    print("    ", end="")
    for i in range(min_longs, max_longs + 1):
        if len(str(i)) == 4:
            print(i, end=" ")
        elif len(str(i)) == 3:
            print(i, end="  ")
        else:
            print(i, end="  ")
        columns += "  |  "

    for j in range(max_lats, min_lats - 1, -1):
        print("\n", "   " + columns, end="")
        print("\n", j, end="")
        for i in range(min_longs, max_longs + 1):
            sym = 0
            for x in range(len(road_map)):
                if i == cities[x][2] and j == cities[x][1]:
                    sym = cities.index(cities[x]) + 1
            if len(str(i)) == 4 and sym is 0:
                print(" - ", end=" ")
            elif len(str(i)) == 3 and sym is 0:
                print(" - ", end="  ")
            elif len(str(i)) == 2 and sym is 0:
                print(" - ", end="   ")
            else:
                print(f" - {sym}", end="  ")
    print("\n" + "   ")


def main():
    print("Type file name: ", end="")
    file = input()
    if os.path.isfile(file):
        print("Initial road map")
        print_cities(file)
        print("\n""Initial road map connections")
        print_map(read_cities(file))
        print("\n""Best cycle")
        best_cycle = find_best_cycle(read_cities(file))
        print(f"{best_cycle} \nBest total distance: {compute_total_distance(best_cycle)}")
        print("\n")
        print(visualise(best_cycle))
    else:
        print("Input file does not exist. Enter correct file name and ensure it is in the same directory as the project files.")


if __name__ == "__main__":  # keep this in
    main()
