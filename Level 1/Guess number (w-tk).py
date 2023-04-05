import random
import tkinter as tk


window = tk.Tk()
window.geometry("300x150")
window.title("Угадай число")


secret_number = 0
attempts = 0
user_number = 0


reset_entry = lambda: entry.delete(0, "end")


def reset_window():
    reset_entry()
    test_button.configure(state=tk.DISABLED)
    reset_button.configure(state=tk.NORMAL)


def set_game_state(state):
    global attempts

    if state == "win":
        label["text"] = "Поздравляю, ты угадал!"
        attempts_label["text"] = f"Правильное число: {secret_number}"
        reset_window()

    elif state == "loose":
        label["text"] = "Можешь сыграть снова!"
        attempts_label["text"] = f"Попытки закончились :("
        reset_window()

    elif state == "not guess":
        if user_number < secret_number:
            label["text"] = "Загаданное число больше!"
        if user_number > secret_number:
            label["text"] = "Загаданное число меньше!"
        attempts_label["text"] = f"Количество попыток: {attempts}"
        reset_entry()

    elif state == "error":
        attempts += 1
        label["text"] = "Введи число от 1 до 100"
        reset_entry()


def test(event):
    global attempts, user_number
    attempts -= 1
    if attempts:
        try:
            user_number = int(entry.get())
            if user_number == secret_number:
                set_game_state("win")
            else:
                set_game_state("not guess")
        except ValueError:
            set_game_state("error")
    else:
        set_game_state("loose")


def new_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 10
    attempts_label["text"] = f"Количество попыток: {attempts}"
    label["text"] = "Угадай число от 1 до 100"

    reset_entry()

    test_button.configure(state=tk.NORMAL)
    reset_button.configure(state=tk.DISABLED)


label = tk.Label(window)
label.place(x=30, y=0)

attempts_label = tk.Label(window)
attempts_label.place(x=30, y=30)

entry = tk.Entry(window)
entry.place(x=40, y=50)
entry.focus_set()

test_button = tk.Button(
    window, text="Проверить", width=17, command=lambda event="<Return>": test(event)
)
test_button.place(x=35, y=80)

reset_button = tk.Button(window, text="Играть снова", width=17, command=new_game)
reset_button.place(x=35, y=110)


new_game()


window.bind("<Return>", test)
window.mainloop()
