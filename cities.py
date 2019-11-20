def read_cities(file_name):
    with open(file_name, "r") as file:
        lines = file.read().splitlines()
        cities = [tuple(line.split("\t")) for line in lines]
        return cities


#road_map = read_cities(file_name)


def convert(N):  # Print only one or two digits after the decimal point
    return float("{0:.2f}".format(float(N)))


def print_cities(road_map):
    #road_map = read_cities(road_map)
    print([(city[1], convert(city[2]), convert(city[3])) for city in road_map])


def compute_total_distance(road_map):
    if not road_map:
        return None
    else:
        # road_map = read_cities(road_map)
        road_map.append(road_map[0])
        road_map = [(city[1], convert(city[2]), convert(city[3])) for city in road_map]
        total_distance = 0.0
        from math import sqrt
        for i in range(len(road_map) - 1):
            lats = road_map[i][1] - road_map[i + 1][1]
            longs = road_map[i][2] - road_map[i + 1][2]
            distance = sqrt(lats ** 2 + longs ** 2)
            total_distance += distance
    return total_distance


def swap_cities(road_map, index1, index2):
    try:
        if index1 == index2:
            print("index1 and index2 are the same!")
        else:
            #new_road_map = read_cities(road_map)
            road_map[index1], road_map[index2] = road_map[index2], road_map[index1]
            new_total_distance = compute_total_distance(road_map)
            #add error handling here (if index1=index2)
            return road_map, new_total_distance
    except IndexError or None:
        print("Index out of range")



def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    first_city_in_new_road_map = road_map[-1]
    return first_city_in_new_road_map


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass


if __name__ == "__main__":  # keep this in
    main()
