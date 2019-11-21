import random, copy, math, os


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
        road_map_copy = [(city[1], convert(city[2]), convert(city[3])) for city in road_map_copy]
        total_distance = 0.0
        for i in range(len(road_map_copy) - 1):
            lats = road_map_copy[i][1] - road_map_copy[i + 1][1]
            longs = road_map_copy[i][2] - road_map_copy[i + 1][2]
            distance = math.sqrt(lats ** 2 + longs ** 2)
            total_distance += distance
    return total_distance


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
    road_map = new_road_map
    return road_map


def find_best_cycle(road_map):
    best_cycle = compute_total_distance(road_map)
    for i in range(10000):
        road_map = shift_cities(road_map)
        swapped = swap_cities(road_map, random.randint(0, len(road_map))-1, random.randint(0, len(road_map)-1))
        if swapped[1] < best_cycle:
            best_cycle = swapped[1]
    return best_cycle


def print_map(road_map):
    road_map = read_cities(road_map)
    road_map.append(road_map[0])
    for i in range(len(road_map) - 1):
        cityA = road_map[i]
        cityB = road_map[i + 1]
        # lats = road_map[i][2] - road_map[i+1][2]
        # longs = road_map[i][3] - road_map[i+1][3]
        # distance = math.sqrt(lats**2 + longs**2)
        distance = math.sqrt((convert(cityA[2]) - convert(cityB[2])) ** 2 + (convert(cityA[3]) - convert(cityB[3])) ** 2)
        print(f"{cityA[1]} ----> {cityB[1]} ===== {distance}")
    print(find_best_cycle(road_map))


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    s = input()
    print_cities(s)
    print_map(s)
    print(compute_total_distance(read_cities(s)))


if __name__ == "__main__":  # keep this in
    main()
