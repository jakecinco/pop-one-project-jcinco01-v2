import tkinter as tk
from cities import *
from swampy.Gui import *

window = Gui()
window.title("GUI")
width_value = window.winfo_screenwidth()
height_value = window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (width_value, height_value))
# window.configure(background='gray80')
label = tk.Label(window, text="Travelling Salesman", fg="white", bg="black", font=("Courier", 30), padx=10, pady=10)
label.pack(fill="x")

canvas = window.ca(width=width_value, height=height_value)
# canvas.configure(scrollregion=canvas.bbox("ALL"))  # Complete window scroll option
canvas.pack()


def linemaker(screen_points):
    """ Function to take list of points and make them into lines
    """
    is_first = True
    # Set up some variables to hold x,y coords
    x0 = y0 = 0
    # Grab each pair of points from the input list
    for (x, y) in screen_points:
        # If its the first point in a set, set x0,y0 to the values
        if is_first:
            x0 = x
            y0 = y
            is_first = False
        else:
            # If its not the fist point yeild previous pair and current pair
            yield x0, y0, x, y
            # Set current x,y to start coords of next line
            x0, y0 = x, y


# def convert_to_pixels(coordinates):
#     new_coords = []
#     for (x, y) in coordinates:
#         lat = (y / (600 / 180) - 90) / -1
#         lng = x / (800 / 360) - 180
#         new_coords.append((lat, lng))
#     return new_coords

#     # lat =(y/(600/180)-90)/-1
#     # lng = x/(800/360)-180



road_map = find_best_cycle(read_cities("city-data.txt"))
map_coords = [(convert(x[2]), convert(x[3])) for x in road_map]  # linemaker accepts list of tuples(x,y)

# new_map_coords = [(latlngToScreenXY(x, y)) for (x, y) in map_coords]
# map_coords = [(x,y) for (x, y, i, j) in new_map_coords]

for (x0, y0, x1, y1) in linemaker(map_coords):
    canvas.line([[x0, y0], [x1, y1]], width=1, arrow="last", fill="red")



print(map_coords)


#
# window.mainloop()

# g = Gui()
# g.title('Gui')
# label = tk.Label(g, text="Travelling Salesman", fg="white", bg="black", font=("Courier", 30), padx=10, pady=10)
# label.pack(fill="x")

# canvas = g.ca(width=400, height=400)
# canvas.create_line(0, 200, 399, 200, dash=(2, 2))  # x-axis
# canvas.create_line(200, 0, 200, 399, dash=(2, 2))  # y-axis

# road_map = find_best_cycle(read_cities("city-data.txt"))  # Returns ([(),()], )
# best_cycle = road_map[0]
# best_cycle.append(best_cycle[0])


# def convert_coordinates(best_cycle):
#     lats = [int(float(city[2])) for city in best_cycle]
#     longs = [int(float(city[3])) for city in best_cycle]
#     min_lats = min(lats)
#     max_lats = max(lats)
#     min_longs = min(longs)
#     max_longs = max(longs)

#     latitudes = []
#     for i in range(max_lats, min_lats - 1, -1):
#         latitudes.append(i)
#     longitudes = []
#     for j in range(min_longs, max_longs + 1, 1):
#         longitudes.append(j)

#     def lat_to_x(lat):
#         return latitudes.index(int(float(lat)))

#     def long_to_y(long):
#         return longitudes.index(int(float(long)))

#     new_map = [(state, city, lat_to_x(lat), long_to_y(long)) for (state, city, lat, long) in best_cycle]
#     return new_map


# def linemaker(screen_points):
#     is_first = True
#     # Set up some variables to hold x,y coords
#     x0 = y0 = 0
#     # Grab each pair of points from the input list
#     for (x, y) in screen_points:
#         # If its the first point in a set, set x0,y0 to the values
#         if is_first:
#             x0 = x
#             y0 = y
#             is_first = False
#         else:
#             # If its not the fist point yeild previous pair and current pair
#             yield x0, y0, x, y
#             # Set current x,y to start coords of next line
#             x0, y0 = x, y


# converted_map = convert_coordinates(best_cycle)

# map_coords = [(x, y) for (a, b, x, y) in converted_map]  # linemaker accepts list of tuples(x,y)

# for (x0, y0, x1, y1) in linemaker(map_coords):
#     canvas.create_line([[x0, y0], [x1, y1]], width=1, arrow="last", activefill="red", tags=(x0, y0))

# distance = tk.Message(window, text=f"Best total distance: {road_map[1]}", width=20)
# distance.pack()

# for (state, city, x, y) in converted_map:
#     canvas.create_text([x*9, y*9], text=state)


window.mainloop()


if __name__ == "__main__":
    main()
