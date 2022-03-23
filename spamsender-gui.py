from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import pyglet
import pyautogui
import time
import threading

# Constants
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# Initial Setup


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


pyglet.font.add_file(str(relative_to_assets("RussoOne-Regular.ttf")))

window = Tk()
window.title("Spamsender: Бомба")

window.geometry("1240x720")
window.configure(bg="#373434")

stop_spam = False
text_to_send = "Lorem"
send_count = 0
delay = 1

# Important mutator functions


def set_sc(sc: int) -> None:
    global send_count
    send_count = sc


def set_txt(txt: str) -> None:
    global text_to_send
    text_to_send = txt


def set_delay(d: float | int) -> None:
    global delay
    delay = d


def send_spam(data: str, send_count: int) -> None:
    time.sleep(10)
    while send_count > 0:
        time.sleep(delay)

        global stop_spam
        if stop_spam:
            break

        pyautogui.write(data)
        pyautogui.press("Enter")
        send_count -= 1

# Create thread for spammer


def create_spammer(data: str, send_count: int) -> None:
    spammer = threading.Thread(target=send_spam, args=(data, send_count))
    spammer.start()


# Stop spamming (No direct thread interaction)
def kill_spammer() -> None:
    global stop_spam
    stop_spam = True


# Create GUI Elements
canvas = Canvas(
    window,
    bg="#373434",
    height=720,
    width=1240,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Title Text
canvas.create_text(
    308.0,
    31.0,
    anchor="nw",
    text="Отправитель спама\n         БОМБИТЬ",
    fill="#FFD43C",
    font=("Russo One", 64 * -1)
)

# Left Radioactivity Logo
image_image_1 = PhotoImage(
    file=relative_to_assets("nuclear_logo1.png"))
image_1 = canvas.create_image(
    105.0,
    112.0,
    image=image_image_1
)

# Right Radioactivity Logo
image_image_2 = PhotoImage(
    file=relative_to_assets("nuclear_logo2.png"))
image_2 = canvas.create_image(
    1123.0,
    112.0,
    image=image_image_2
)

# entry is textArea or textBox

# Label text for Entry 1
canvas.create_text(
    20.0,
    343.0,
    anchor="nw",
    text="Код 1\nCode 1 (Text)",
    fill="#FFFFFF",
    font=("Russo One", 30 * -1)
)

# Entry 1 (Text to send)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    554.5,
    379.0,
    image=entry_image_1
)
entry1_code1 = Text(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    font=("Courier", 16, "bold")
)
entry1_code1.place(
    x=294.0,
    y=351.0,
    width=521.0,
    height=54.0
)

# Confirm button for Entry 1
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button1_confirm_code1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_txt(str(entry1_code1.get("1.0", "end-1c"))),
    relief="flat"
)
button1_confirm_code1.place(
    x=873.0,
    y=345.0,
    width=336.0,
    height=69.0
)

# Label Text for Entry 2
canvas.create_text(
    14.0,
    431.0,
    anchor="nw",
    text="Код 2\nCode 2 (Count)",
    fill="#FFFFFF",
    font=("Russo One", 30 * -1)
)

# Entry 2 (Send Count)
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    554.5,
    467.0,
    image=entry_image_2
)
entry2_code2 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    font=("Courier", 16, "bold")
)
entry2_code2.place(
    x=294.0,
    y=439.0,
    width=521.0,
    height=54.0
)

# Confirm button for Entry 2
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button2_confirm_code2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_sc(int(entry2_code2.get())),
    relief="flat"
)
button2_confirm_code2.place(
    x=873.0,
    y=432.0,
    width=336.0,
    height=69.0
)

# Label Text for Entry 3
canvas.create_text(
    42.0,
    257.0,
    anchor="nw",
    text="задержка\nDelay (sec)",
    fill="#FFFFFF",
    font=("Russo One", 30 * -1)
)

# Entry 3 (Delay), ! Placed BEFORE Entry 1
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    554.5,
    291.0,
    image=entry_image_3
)
entry3_delaysec = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    font=("Courier", 16, "bold")
)
entry3_delaysec.place(
    x=294.0,
    y=263.0,
    width=521.0,
    height=54.0
)

# Confirm button for Entry 3
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button3_confirm_delay = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_delay(float(entry3_delaysec.get())),
    relief="flat"
)
button3_confirm_delay.place(
    x=873.0,
    y=257.0,
    width=336.0,
    height=69.0
)

# LAUNCH Button (Start spammer with given details)
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button4_createspammer_launch = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: create_spammer(data=text_to_send, send_count=send_count),
    relief="flat"
)
button4_createspammer_launch.place(
    x=124.0,
    y=567.0,
    width=340.0,
    height=130.0
)

# ABORT Button (Kill spammer)
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button5_killspammer_abort = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: kill_spammer(),
    relief="flat"
)
button5_killspammer_abort.place(
    x=769.0,
    y=567.0,
    width=340.0,
    height=130.0
)

# Resizability false because it will mess up the layout of elements
window.resizable(False, False)
window.mainloop()
