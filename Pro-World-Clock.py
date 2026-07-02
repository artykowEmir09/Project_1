import tkinter as tk
from time import strftime
from datetime import datetime
import math
import pytz

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("World Clock Pro")
root.geometry("500x500")

theme = {"bg": "#1e1e2f", "fg": "white"}

# ---------------- CANVAS (circle clock) ----------------
canvas = tk.Canvas(root, width=300, height=300, bg=theme["bg"], highlightthickness=0)
canvas.pack(pady=20)

# ---------------- DIGITAL LABEL ----------------
label = tk.Label(root, font=("Arial", 20), bg=theme["bg"], fg="white")
label.pack()

# ---------------- TIMEZONE ----------------
cities = {
    "Malaysia": "Asia/Kuala_Lumpur",
    "UK": "Europe/London",
    "USA (NY)": "America/New_York",
    "Japan": "Asia/Tokyo"
}

selected_city = tk.StringVar(value="Malaysia")

dropdown = tk.OptionMenu(root, selected_city, *cities.keys())
dropdown.pack()


# ---------------- DIGITAL TIME ----------------
def update_time():
    city = cities[selected_city.get()]
    tz = pytz.timezone(city)
    now = datetime.now(tz)

    time_str = now.strftime("%H:%M:%S")
    label.config(text=f"{selected_city.get()} : {time_str}")

    draw_clock(now)

    root.after(1000, update_time)


# ---------------- ANALOG CLOCK ----------------
def draw_clock(now):
    canvas.delete("all")

    cx, cy = 150, 150
    r = 100

    # circle
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="white")

    # numbers
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = cx + math.cos(angle) * (r - 20)
        y = cy + math.sin(angle) * (r - 20)
        canvas.create_text(x, y, text=str(i), fill="white")

    h = now.hour % 12
    m = now.minute
    s = now.second

    # hour hand
    draw_hand(cx, cy, (h + m/60) * 30, 50, "white")
    # minute hand
    draw_hand(cx, cy, m * 6, 70, "white")
    # second hand
    draw_hand(cx, cy, s * 6, 90, "red")


def draw_hand(cx, cy, angle, length, color):
    angle = math.radians(angle - 90)
    x = cx + math.cos(angle) * length
    y = cy + math.sin(angle) * length
    canvas.create_line(cx, cy, x, y, fill=color, width=2)


# ---------------- THEME ----------------
def dark_theme():
    theme["bg"] = "#1e1e2f"
    canvas.config(bg=theme["bg"])
    label.config(bg=theme["bg"], fg="white")


def light_theme():
    theme["bg"] = "white"
    canvas.config(bg=theme["bg"])
    label.config(bg="white", fg="black")


menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Dark", command=dark_theme)
theme_menu.add_command(label="Light", command=light_theme)

menubar.add_cascade(label="Theme", menu=theme_menu)
root.config(menu=menubar)

update_time()
root.mainloop()
