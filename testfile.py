from cities import *
import tkinter as tk

window = tk.Tk()
window.title("GUI")
window.geometry("800x600")
# window.configure(background='gray80')
label = tk.Label(window, text="Travelling Salesman", fg="white", bg="black", font=("Courier", 30), padx=10, pady=10)
label.pack(fill="x")


def printSomething():
    road_map = read_cities("city-data.txt")
    best_cycle = find_best_cycle(road_map)
    w = tk.Message(window, text=f"Best total distance: {best_cycle[1]}", width=200)
    w.pack()
    for city in best_cycle[0]:  # 0 is unnecessary
        state = f"{city[0]}, {city[1]}  ----->   {city[2]} {city[3]}"
        label = tk.Label(window, text=state, font=("Helvetica", 9), anchor="center", justify="center")
        # this creates x as a new label to the GUI
        label.pack()


button = tk.Button(window, text="Print Map", command=printSomething, relief="sunken")
button.pack()

window.mainloop()
