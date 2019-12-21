import math
import random
import os.path


def read_cities(file_name):
    """Read in the cities from the given file_name, and return them as a list of four-tuples:"""
    with open(file_name, "r") as file:
        lines = file.read().splitlines()
        cities = [tuple(line.split("\t")) for line in lines]
        return cities


def convert(num):
    """Convert string to 2-decimal place float"""
    try:
        return float("{0:.2f}".format(float(num)))
    except ValueError:
        print("Cannot convert non-numerical strings to float.")
        raise


def print_cities(road_map):
    """Prints a list of cities, along with their locations. Print up to two digits after the decimal point."""
    road_map = read_cities(road_map)
    cities = [(city[0], city[1], convert(city[2]), convert(city[3])) for city in road_map]
    print(cities)


def compute_total_distance(road_map):
    """Returns, as a floating point number, the sum of the distances of all the connections in the road_map.
    Remember that it's a cycle, so that for example in the initial road_map above, Wyoming connects to Alabama..."""
    try:
        if not road_map:
            return None
        else:
            map_copy = [*road_map, road_map[0]]
            total_distance = 0.0
            for i in range(len(map_copy) - 1):
                lats = float(map_copy[i][2]) - float(map_copy[i + 1][2])
                longs = float(map_copy[i][3]) - float(map_copy[i + 1][3])
                distance = math.sqrt(lats * lats + longs * longs)
                total_distance += distance
        return convert(total_distance)
    except TypeError as error:
        print(error)
        raise


def swap_cities(road_map, index1, index2):
    """Take the city at location index in the road_map, and the city at location index2,
    swap their positions in the road_map, compute the new total distance, and return the tuple"""
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
    """For every index i in the road_map, the city at the position i moves to the position i+1.
    The city at the last position moves to the position 0. Return the the new road map."""
    try:
        new_road_map = [road_map[-1]]
        new_road_map.extend(road_map[:-1])
        return new_road_map
    except TypeError or None:
        print("No road map provided.")


def find_best_cycle(road_map):
    """Using a combination of swap_cities and shift_cities, try 10000 swaps/shifts, and each time keep
    the best cycle found so far. After 10000 swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping."""
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
    """Prints, in an easily understandable textual format, the cities and their connections, along with
    the cost for each connection and the total cost."""
    map_copy = road_map[:]
    map_copy.append(road_map[0])
    for i in range(len(map_copy) - 1):
        cityA = map_copy[i]
        cityB = map_copy[i + 1]
        distance = math.sqrt((float(cityA[2]) - float(cityB[2])) ** 2 + (float(cityA[3]) - float(cityB[3])) ** 2)
        print(f"{cityA[0], cityA[1]} -----> {cityB[0], cityB[1]} ===== {convert(distance)}")
    print(f"TOTAL DISTANCE: {convert(compute_total_distance(map_copy))}")


def visualise(road_map):
    """Use textual printing to visualise the map"""
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
                print(" - ", end="  ")
            elif len(str(i)) == 3 and sym is 0:
                print(" - ", end="  ")
            elif len(str(i)) == 2 and sym is 0:
                print(" - ", end="   ")
            else:
                print(f" - {sym}", end="")
    print("\n" + "   ")


def main():
    """Requests to specify the file to load (make sure the file exists and valid), reads in
    and prints out the city data, creates the "best" cycle, prints it out."""
    print("Type file name: ", end="")
    file = input()
    if os.path.isfile(file):
        print("INITIAL ROAD MAP:")
        print_cities(file)
        print("\n""ROAD MAP CONNECTIONS:")
        print_map(read_cities(file))
        print("\n""BEST CYCLE:")
        best_cycle = find_best_cycle(read_cities(file))
        print_map(best_cycle)
        print("\n")
        visualise(best_cycle)
    else:
        print("Input file does not exist. "
              "Enter correct file name and ensure it is in the same directory as the project files.")


if __name__ == "__main__":  # keep this in
    main()
