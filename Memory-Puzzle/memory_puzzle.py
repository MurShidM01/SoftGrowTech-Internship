import tkinter as tk
import random

ROWS = 4
COLS = 4
TIME_LIMIT = 60

emojis = ["🍎","🍓","🍋","🍇","🍉","🍑","🥝","🍒"]

root = tk.Tk()
root.title("Memory Puzzle")
root.geometry("420x520")
root.configure(bg="#f6f8fb")

time_left = TIME_LIMIT
timer_id = None

first = None
second = None
lock = False
game_over = False

cards = []
matched = []
buttons = []

# ---------------- UI ----------------

title = tk.Label(root,text="🧠 Memory Puzzle",
                 font=("Segoe UI",20,"bold"),
                 bg="#f6f8fb")
title.pack(pady=10)

timer_label = tk.Label(root,font=("Segoe UI",14),
                       bg="#f6f8fb")
timer_label.pack()

frame = tk.Frame(root,bg="#f6f8fb")
frame.pack(expand=True,fill="both",padx=15,pady=15)

for r in range(ROWS):
    frame.rowconfigure(r,weight=1)

for c in range(COLS):
    frame.columnconfigure(c,weight=1)


# -------------- GAME FUNCTIONS ----------------

def start_game():

    global cards, matched, time_left, first, second, lock, game_over, timer_id

    if timer_id:
        root.after_cancel(timer_id)

    play_again.place_forget()

    time_left = TIME_LIMIT
    first = None
    second = None
    lock = False
    game_over = False

    cards = emojis * 2
    random.shuffle(cards)

    matched = [False]*len(cards)

    for i,btn in enumerate(buttons):
        btn.config(text="❔",bg="white",state="normal",
                   command=lambda i=i: flip(i))

    update_timer()


def flip(index):

    global first, second, lock

    if lock or matched[index] or game_over:
        return

    buttons[index]["text"] = cards[index]
    buttons[index]["bg"] = "#ecf4ff"

    if first is None:
        first = index

    elif second is None and index != first:
        second = index
        lock = True
        root.after(600,check_match)


def check_match():

    global first, second, lock

    i = first
    j = second

    if cards[i] == cards[j]:

        matched[i] = True
        matched[j] = True

        buttons[i]["bg"] = "#d4f8d4"
        buttons[j]["bg"] = "#d4f8d4"

    else:

        buttons[i]["text"] = "❔"
        buttons[j]["text"] = "❔"

        buttons[i]["bg"] = "white"
        buttons[j]["bg"] = "white"

    first = None
    second = None
    lock = False

    if all(matched):
        timer_label.config(text="🎉 You Win!")
        end_game()


def update_timer():

    global time_left, timer_id

    if game_over:
        return

    if time_left > 0:
        timer_label.config(text=f"⏱ {time_left}s")
        time_left -= 1
        timer_id = root.after(1000,update_timer)

    else:
        timer_label.config(text="⌛ Time's Up!")
        end_game()


def end_game():

    global game_over

    game_over = True

    if timer_id:
        root.after_cancel(timer_id)

    for btn in buttons:
        btn.config(state="disabled")

    play_again.place(relx=0.5,rely=0.94,anchor="center")


# -------------- CREATE BUTTON GRID ----------------

for r in range(ROWS):
    for c in range(COLS):

        btn = tk.Button(frame,
                        text="❔",
                        font=("Segoe UI Emoji",28),
                        bg="white",
                        relief="flat")

        btn.grid(row=r,column=c,padx=6,pady=6,sticky="nsew")

        buttons.append(btn)


play_again = tk.Button(root,
                       text="🔄 Play Again",
                       font=("Segoe UI",13,"bold"),
                       bg="#4da3ff",
                       fg="white",
                       relief="flat",
                       command=start_game)


start_game()

root.mainloop()