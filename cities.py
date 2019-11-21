import random, copy, math, os


def read_cities(file_name):
    with open(file_name, "r") as file:
        lines = file.read().splitlines()
        cities = [tuple(line.split("\t")) for line in lines]
        return cities


def convert(N):  # Print only one or two digits after the decimal point
    return float("{0:.2f}".format(float(N)))


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
        # road_map = read_cities(road_map)
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
        if index1 == index2:
            index1 = random.randint(0, len(road_map))
        else:
            map_copy = copy.deepcopy(road_map)
            map_copy[index1], map_copy[index2] = map_copy[index2], map_copy[index1]
            new_total_distance = compute_total_distance(map_copy)
            # road_map[index1], road_map[index2] = road_map[index2], road_map[index1]
            # new_total_distance = compute_total_distance(road_map)
            return map_copy, new_total_distance
    except IndexError or None:
        print("Index out of range")


def shift_cities(road_map):
    new_road_map = [road_map[-1]]
    new_road_map.extend(road_map[:-1])
    road_map = new_road_map
    return road_map


def find_best_cycle(road_map):
    map_copy = copy.deepcopy(road_map)
    best_cycle = compute_total_distance(map_copy)
    best_map = []
    for i in range(10000):
        swap_cities(map_copy, random.randint(0, len(map_copy)), random.randint(0, len(map_copy)))
        map_copy = shift_cities(map_copy)
        total_distance = compute_total_distance(map_copy)
        if best_cycle > total_distance:
            best_cycle = total_distance
            best_map = copy.deepcopy(map_copy)
    return best_cycle


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
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


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    s = input()
    print_cities(s)
    print_map(s)


if __name__ == "__main__":  # keep this in
    main()
