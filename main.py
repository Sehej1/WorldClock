import tkinter as tk
import requests


def get_time(country, label):
    link = "https://www.timeapi.io/api/Time/current/zone?"
    parameters = {"timezone": country}
    clock = requests.get(url=link, params=parameters).json()

    try:
        zone = clock["timeZone"]
        name = zone[zone.index("/") + 1:]
        time = clock["time"]
        seconds = clock["seconds"]
        date = clock["date"]
        str_time = f"In {name}, it is currently: {time}:{seconds} \nThe date is: {date}"
    except TypeError:
        str_time = "That timezone does not exist."

    label['text'] = str_time


def main():
    root = tk.Tk()
    root.title("World Clock")

    HEIGHT, WIDTH = 600, 700
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#241f1c")
    canvas.pack()

    title = tk.Label(canvas, text="World Clock", bg="#241f1c", font=("Times New Roman", 35), fg="#ebebde")
    title.place(relx=0.33, rely=0.05)

    # Upper Frame
    frame = tk.Frame(root, bd=5, bg="#ebebde")
    frame.place(relx=0.05, rely=0.19, relwidth=0.9, relheight=0.08)

    note = tk.Label(frame, text="Enter timezone:", font=("Times New Roman", 13), bg="#ebebde")
    note.place(rely=0.1)

    country = tk.Entry(frame, bd="2")
    country.place(relx=0.19, rely=0.1, relwidth=0.35, relheight=0.8)

    go = tk.Button(frame, text="Get time", bg="white",
                   command=lambda: get_time(country.get(), worldTime))  # Call function
    go.place(relx=0.65, rely=0.1, relwidth=0.35, relheight=0.8)

    # Lower Frame
    bottom_frame = tk.Frame(root, bg="#ebebde")
    bottom_frame.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.65)

    worldTime = tk.Label(bottom_frame, font=("Times New Roman", 15))
    worldTime.place(relx=0.03, rely=0.08, relwidth=0.93, relheight=0.84)

    root.mainloop()


main()
